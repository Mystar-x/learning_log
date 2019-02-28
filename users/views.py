from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def logout_view(request):
    """注销用户"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))

def  register(request):
    """注册新用户"""
    if request.method !='POST':
        #显示空的注册表单
        form = UserCreationForm()
    else:
        #处理填写好的表单
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()#用户输入的有效的情况下，将其用户名和密码存入数据库中，并返回一个用户对象
            #让用户自动登陆，再重新定向到主页
            authenticated_user = authenticate(username=new_user.username,
                password = request.POST['password1'])#由于两次提交的密码都有效，这里就用了password1
            login(request, authenticated_user)#通过了authenticate验证的用户对象存储在authenticated_user中
            return HttpResponseRedirect(reverse('learning_logs:index'))

    context = {'form': form}
    return render(request, 'users/register.html', context)