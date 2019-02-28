"""定义learning_logs的URL模式"""
from django.conf.urls import url
from . import views
#1 定义url
#2 编写视图函数
#3 编写模板
#4 链接到网页
app_name = 'learning_logs'#这里有点儿重要啊，没有皮儿子的这个提示，就运行不了
urlpatterns= [
    #主页
    url(r'^$', views.index, name='index'),
    #显示所有主题
    url(r'^topics/$', views.topics, name='topics'),
    #特定主题的详细页面
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    #用于添加新主题的网页
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    #用于添加新条目的网页
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    #用于编辑条目的页面
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),

]
#r'^$' 为正则表达式，r让python将接下来的字符串视为原始字符串，引号标识正则表达式
#的起始位置，^让python查看字符串的开头，$让其查看字符串的末尾。
#可见，这个正则表达式让python查找开头和末尾之间没有任何东西的url，localhost:8000
#与第一个正则表达式相匹配
#第二个正则表达式匹配的为 基础url+topics
#第三个正则表达式中/ /之间的表达式与url中的这部分的整数(主题id)匹配，将整数存储在
#topic_id中，括号捕获url中的整数的值，?P<topic_id>将匹配的值存储在topic_id中