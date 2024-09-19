from django.contrib import admin
from django.urls import path
from MyStudent import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.MyLogin),
    path('signup/',views.MySignUp),
    path('admindash/',views.MyAdmin),
    path('userdash/',views.MyUser),
    path('studreg/',views.StudReg),
    path('userstudview/',views.UserStudView),
    path('adminstudview/',views.AdminStudView),
    path('adminnotice/',views.AdminNotice1),
    path('noticeremove/',views.NoticeRemove),
    path('noticeupdate/',views.NoticeUpdate,name='noticeupdate'),
    path('adminnoticeview/',views.AdminNoticeView),
    path('usernoticeview/',views.UserNoticeView),
    path('userstudremove',views.UserStudRemove),
    path('studupdate/',views.StudUpdate),
]
