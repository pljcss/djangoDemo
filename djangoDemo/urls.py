"""djangoDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
import xadmin
from django.conf.urls import url
from polls.views import getform
from django.views.generic import TemplateView
from edu_users import views
from edu_users.views import LoginView, RegisterView, ActiveUserView, ForgetPwdView, ResetView, ModifyPwdView

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('xadmin', xadmin.site.urls),

    path('', TemplateView.as_view(template_name='edu_index.html'),name='index'),
    # path('login/', TemplateView.as_view(template_name='edu_login.html'), name='login'),

    path('login/', LoginView.as_view(), name='login'), # 修改login路由
    path('register/',RegisterView.as_view(),name = 'register'), # 注册页面
    path('captcha/',include('captcha.urls')), # 验证码

    re_path('active/(?P<active_code>.*)/', ActiveUserView.as_view(), name='user_active'),

    path('forget/',ForgetPwdView.as_view(),name='forget_pwd'), # 忘记密码

    re_path('reset/(?P<active_code>.*)/', ResetView.as_view(), name='reset_pwd'),

    path('modify_pwd/', ModifyPwdView.as_view(), name='modify_pwd'),
]
