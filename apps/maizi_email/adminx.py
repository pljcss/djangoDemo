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



class EmailSendAdmin(object):
    list_display = ['name', 'email', 'to_user']
    filter_horizontal = ['to_user', ]  # 给多选增加一个左右添加的框
    # object_list_template = "self_mail_assist.html"
    style_fields = {'to_user': 'm2m_transfer'}

xadmin.site.register(EmailSend, EmailSendAdmin)




class UserEmailAdmin(object):
    list_display = ['email_address']

xadmin.site.register(UserEmail, UserEmailAdmin)