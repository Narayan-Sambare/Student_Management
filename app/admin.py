from django.contrib import admin
from app.models import SignUp
from app.models import studentreg,AdminNotice

# Register your models here.

admin.site.register(SignUp)
admin.site.register(studentreg)
admin.site.register(AdminNotice)
