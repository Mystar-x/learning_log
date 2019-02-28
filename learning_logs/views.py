from django.shortcuts import render
from .models import Topic, Entry
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    """学习笔记的主页"""
    return render(request, 'learning_logs/index.html')

@login_required#这个函数作为装饰器，再加上@，使得python在运行后面的函数前，先运行这个函数，这个函数检查用户是否已登录，未登录时
#我们应将页面重定向至登陆页面，所以应该修改settings.py
#注意，这个@只能管住它后面的一个函数，因此后面所有的都加了这个限制
def topics(request):
    """显示所有主题"""
    topics = Topic.objects.filter(owner=request.user).order_by('data_added')#让Django只从数据库中获取owner属性为当前用户的Topic对象
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """显示单个主题及其所有条目"""
    topic = Topic.objects.get(id = topic_id)
    #确认请求的主题属于当前用户,防止不是正确用户登陆的情况下直接输入相应网址去查看主题内容
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries':entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        #未提交数据，创建一个新表单
        form = TopicForm()
    else:
        #POST提交的数据，对数据进行处理
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user#将新主题的owner属性设置为当前用户
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    context = {'form':form}
    return render(request, 'learning_logs/new_topic.html', context)
    #2019/2/23  learning_logs:topics无法重定向是怎么回事？
    #2019/2/24  new_topic.html中 form错打成from！！！！！！！

@login_required
def new_entry(request, topic_id):
    """在特定的主题中添加新条目"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        #未提交数据，返回一个新表单
        form = EntryForm()
    else:
        #POST提交的数据，对数据进行处理
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)#False使得Django创建一个新条目对象，并将其存储到new_entry中，但不保存到数据库中
            new_entry.topic = topic#new_entry的属性topic设置为函数开头从数据库中获取的主题
            new_entry.save()#保存到数据库
            return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic_id]))#reverse两个实参，一个是topic，一个是topic_id
    context = {'topic':topic, 'form':form }
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """编辑既有条目"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        #初次请求，使用当前条目填充表单
        form = EntryForm(instance=entry)#创建一个表单，并用既有条目对象的信息填充它，用户将看到既有数据，并能够编辑，注意与上面的区别
    else:
        #POST提交的数据，对数据进行处理
        form = EntryForm(instance=entry, data=request.POST)#创建一个表单实例，并根据request.POST中的相关数据对其进行修改
        if form.is_valid():#
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))
    context = {'entry':entry, 'topic':topic, 'form':form}
    return render(request, 'learning_logs/edit_entry.html', context)