from django.shortcuts import render,redirect
from .models import Student_model
from .forms import Student_form

def home(request):
    data = Student_model.objects.all()
    data_dict = {"data_list":data} 
    # return render(request,"studentmanager/home.html",context = data_dict)
    return render(request,"studentmanager/home.html",context = data_dict)

def Add_student(request):
    form = Student_form()
    if request.method == "POST":
        form = Student_form(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect("/home")
    return render(request,"studentmanager/add.html", context={"form":form})

def delete_student(request,id):
    student = Student_model.objects.get(id=id)
    student.delete()
    return redirect("/home")

def update_student(request,id):
    student = Student_model.objects.get(id=id)
    print(student)
    if request.method == "POST":
        form = Student_form(request.POST,instance=student)
        print(form)
        if form.is_valid():
            print("i reached isvalid")
            form.save()
            return redirect("/home")
    return render(request, "studentmanager/update.html",{"student":student})

