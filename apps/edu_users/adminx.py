import xadmin
from .models import EmailVerifyRecord, Banner
from xadmin import views


#xadmin中这里是继承object，不再是继承admin
class EmailVerifyRecordAdmin(object):
    # 显示的列
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 搜索的字段，不要添加时间搜索
    search_fields = ['code', 'email', 'send_type']
    # 过滤
    list_filter = ['code', 'email', 'send_type', 'send_time']

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)


class BannerAdmin(object):
    list_display = ['title', 'image', 'url','index', 'add_time']
    search_fields = ['title', 'image', 'url','index']
    list_filter = ['title', 'image', 'url','index', 'add_time']


xadmin.site.register(Banner,BannerAdmin)



# 创建xadmin的最基本管理器配置，并与view绑定
class BaseSetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True

# 将基本配置管理与view绑定
xadmin.site.register(views.BaseAdminView,BaseSetting)

# 全局修改，固定写法
class GlobalSettings(object): # 名称不能改
    # 修改title
    site_title = 'Demo 管理'
    # 修改footer
    site_footer = 'coo'
    # 收起菜单
    menu_style = 'accordion'

    ##### 设计左侧菜单
    def get_site_menu(self):  # 名称不能改
        return [
            {
                'title': '自定义菜单',
                'icon': 'fa fa-bar-chart-o',
                'menus': (
                    {
                        'title': '子自定义菜单1',    # 这里是你菜单的名称
                        'url': '/xadmin/test_view',     # 这里填写你将要跳转url
                        'icon': 'fa fa-cny'     # 这里是bootstrap的icon类名，要换icon只要登录bootstrap官网找到icon的对应类名换上即可
                    },
                    {
                        'title': '子自定义菜单2',
                        'url': 'http://www.taobao.com',
                        'icon': 'fa fa-cny'
                    }
                )
            }
        ]


# 注册上面填写的url
from custom_page.views import TestView   #从你的app的view里引入你将要写的view，你也可以另外写一个py文件，把后台的view集中在一起方便管理
xadmin.site.register_view(r'test_view/$', TestView, name='for_test')


# 将title和footer信息进行注册
# 注册自定义菜单
xadmin.site.register(views.CommAdminView,GlobalSettings)