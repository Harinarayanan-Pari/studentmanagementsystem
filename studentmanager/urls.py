from django.urls import path
from . import views

urlpatterns = [
    path("",views.home),
    path("home/",views.home),
    path("add/",views.Add_student),
    path("delete/<id>",views.delete_student),
    path("update/<id>",views.update_student)
]