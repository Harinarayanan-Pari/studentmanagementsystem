from django.contrib import admin
from .models import Student_model
# Register your models here.
# class Student_Admin(admin.ModelAdmin):
#     obj = ["name","age",]
admin.site.register(Student_model)