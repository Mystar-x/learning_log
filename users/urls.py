"""为应用程序users定义url模式"""

from django.conf.urls import url
from django.contrib.auth.views import LoginView
from django.urls import path
from . import views
app_name = 'users'
urlpatterns =[
    #登陆页面
    url(r'^login/$', LoginView.as_view(template_name = 'users/login.html'), name="login"), 
    #path('login/', LoginView.as_view(template_name='users/login.html'), name="login"),
    #注销
    url(r'^logout/$', views.logout_view, name='logout'),
    #注册页面
    url(r'^register/$', views.register, name='register'),
    
    ]
 #这里没有用自己的view.login视图函数，而是采用的默认的login视图