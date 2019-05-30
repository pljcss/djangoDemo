from .models import EmailSend
import xadmin

class EmailSendAdmin:
    list_display = [ 'name', 'email']

# 将管理器与model进行注册关联
xadmin.site.register(EmailSend, EmailSendAdmin)