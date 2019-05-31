from .models import EmailSend
import xadmin
from edu_course.models import UserEmail
# class EmailSendAdmin:
#     list_display = [ 'name', 'email']
#
# # 将管理器与model进行注册关联
# xadmin.site.register(EmailSend, EmailSendAdmin)
#
# from .views import testView
#
#
# xadmin.site.register_view(r'test_view/$', testView, name='for_test')


#
# class EmailSendAdmin(object):
#     list_display = ['name', 'email', 'to_user']
#     filter_horizontal = ['to_user', ]  # 给多选增加一个左右添加的框
#     # object_list_template = "self_mail_assist.html"
#     style_fields = {'to_user': 'm2m_transfer'}
#
# # xadmin.site.register(EmailSend, EmailSendAdmin)
# xadmin.site.register(EmailSend, EmailSendAdmin)
#
#
#
# class UserEmailAdmin(object):
#     """
#     发送邮件
#     """
#     list_display = ['email_address']
#
# xadmin.site.register(UserEmail, UserEmailAdmin)





# 注册你上面填写的url
# from custom_page.views import TestView

# 从你的app的view里引入你将要写的view，你也可以另外写一个py文件，把后台的view集中在一起方便管理
# xadmin.site.register_view(r'test_view/$', TestView, name='for_test')

# 注册GlobalSetting
from xadmin.views import CommAdminView
# xadmin.site.register(CommAdminView, GlobalSetting)

from .views import testView
xadmin.site.register_view(r'test_view/$', testView, name='for_test')
