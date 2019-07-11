from django.contrib import admin

from .models import Student

class Studentadmin(admin.ModelAdmin):
    list_display = ('sid','sname','saddress')


admin.site.register(Student,Studentadmin)
admin.site.site_header='MANI KUMAR'