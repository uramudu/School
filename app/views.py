from django.shortcuts import render,redirect
from django.views.generic import ListView,CreateView,UpdateView,DetailView,DeleteView
from .models import Student
from .models import Chart
from .models import Chart1
from .models import Teacher
from .models import Std
def index(request):
    return render(request,"index.html")
def send(request):
    idno=request.POST.get("idno")
    name=request.POST.get("name")
    surname=request.POST.get("surname")
    father=request.POST.get("father")
    mother=request.POST.get("mother")
    date=request.POST.get("date")
    gen=request.POST.get("gen")
    phone=request.POST.get("phone")
    username=request.POST.get("username")
    password=request.POST.get("password")
    image = request.POST.get("image")
    section=request.POST.get("section")
    image = request.FILES["image"]
    Student(idno=idno,name=name,surname=surname,father=father,mother=mother,date=date,gen=gen,phone=phone,username=username,password=password,image=image).save()
    return render(request,"AllDetails.html",{"message":"successfull Register"})


def show(request):
    qs = Student.objects.all()
    return render(request,"details.html",{"data":qs})


class Allstudent(ListView):
    template_name = "all.html"
    model = Student
    queryset = Student.objects.values("idno")


class OneEmployee(DetailView):
    model = Student
    template_name = "Profile.html"



def login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        qs=Student.objects.filter(username=username,password=password)
        if qs:
            request.session["token"]=username
            return render(request,"AllDetails.html")
        else:
            return render(request,"Login.html",{"message":"Invalid"})


def chart(request):
    num=request.POST.get("num")
    quection=request.POST.get("quection")
    Chart(num=num,quection=quection).save()
    return render(request,"Question.html",{"messgae":"successfull Posted"})


def Tea(request):
    name=request.POST.get("name")
    date=request.POST.get("date")
    gen=request.POST.get("gen")
    sub=request.POST.get("sub")
    phone=request.POST.get("phone")
    username=request.POST.get("username")
    password=request.POST.get("password")
    Teacher(name=name,date=date,gen=gen,sub=sub,phone=phone,username=username,password=password).save()
    return render(request,"Teacher1.html",{"message":"Successfull Register"})


def tlogin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        qs = Teacher.objects.filter(username=username, password=password)
        if qs:
            request.session["Rmd"] = username
            return render(request, "Teacher1.html")
        else:
            return render(request, "TeacherLogin.html", {"message": "Invalid"})

class Show(CreateView):
    model =Std
    template_name = "index2.html"
    fields = ["num","Answer"]
    success_url = "/Ram/"


class Update(UpdateView):
    model = Std
    template_name = "Update.html"
    fields = ["num","Answer"]
    success_url = "/Ram/"


class Delete(DeleteView):
    model = Std
    template_name = "Delete.html"
    fields = ["num","Answer"]
    success_url = "/Ram/"


class Detail(ListView):
   template_name = "StudentQuection.html"
   model = Chart

#def details(request):
#    num=request.POST.get("num")
#    quection=request.POST.get("quection")
#    d={"nem":num,"quection":quection}
#    return render(request,"StudentQuection.html",d)
class TeaDetail(ListView):
    template_name = "TeacherQuection.html"
    model = Std


def logout(request):
    del request.session['token']
    request.session.modified=True
    return redirect("index1")

def tlogout(request):
    del request.session['Rmd']
    request.session.modified=True
    return redirect("index1")
"""
class TeaShow(CreateView):
    model = Chart
    template_name = "TeaherHome.html"
    fields = ["num","quection"]
    success_url = "/Tea1/"


class TeaUp(UpdateView):
    model = Chart
    template_name = "TeaUp.html"
    fields = ["num","quection"]
    success_url = "/Tea1/"


class TeaDel(DeleteView):
    model = Chart
    template_name = "TeaDel.html"
    fields = ["num","quection"]
    success_url = "/Tea1/"

"""
