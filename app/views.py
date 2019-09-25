from django.shortcuts import render,redirect
from django.views.generic import ListView,CreateView,UpdateView,DetailView,DeleteView
from .models import Student
from .models import Chart
from .models import Chart1
from .models import Teacher
from .models import Std
from .models import Exam2
from .models import Exam3
from .models import Answer
import re
from django.contrib.auth.decorators import login_required

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
    a = re.fullmatch("[6-9]\d{9}", phone)
    b = re.fullmatch("\w[a-zA-Z0-9_.]*[@#$]", username)
    c = re.fullmatch("[a-zA-Z0-9]{6,9}", password)
    d = re.fullmatch("[0-9]\d{4}",idno)
    if (a and b and c and d) != None:
        Student(idno=idno,name=name,surname=surname,father=father,mother=mother,date=date,gen=gen,phone=phone,username=username,password=password,image=image,section=section).save()
        return render(request,"AllDetails.html",{"message":"successfull Register"})
    else:
        return render(request, "index.html")


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
    fields = ["num","Answer",]
    success_url = "/Ram/"




class Delete(DeleteView):
    model = Std
    template_name = "Delete.html"
    fields = ["num","Answer"]
    success_url = "/Ram/"



class Detail(ListView):
   template_name = "StudentQuection.html"
   model = Chart

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



def images(request):
    return render(request,"Rmd.html")




def exam1(request):
    return render(request,"Exam.html")


def exam2(request):
    idno=request.POST.get("idno")
    que1=request.POST.get("que1")
    que2=request.POST.get("que2")
    que3=request.POST.get("que3")
    que4=request.POST.get("que4")
    que5=request.POST.get("que5")
    que6=request.POST.get("que6")
    que7=request.POST.get("que7")
    que8=request.POST.get("que8")
    que9=request.POST.get("que9")
    que10=request.POST.get("que10")
    ans1=request.POST.get("ans1")
    ans2=request.POST.get("ans2")
    ans3=request.POST.get("ans3")
    ans4=request.POST.get("ans4")
    ans5=request.POST.get("ans5")
    ans6=request.POST.get("ans6")
    ans7=request.POST.get("ans7")
    ans8=request.POST.get("ans8")
    ans9=request.POST.get("ans9")
    ans10=request.POST.get("ans10")
    ans11=request.POST.get("ans11")
    ans12=request.POST.get("ans12")
    ans13=request.POST.get("ans13")
    ans14=request.POST.get("ans14")
    ans15=request.POST.get("ans15")
    ans16=request.POST.get("ans16")
    ans17=request.POST.get("ans17")
    ans18=request.POST.get("ans18")
    ans19=request.POST.get("ans19")
    ans20=request.POST.get("ans20")
    ans21=request.POST.get("ans21")
    ans22=request.POST.get("ans22")
    ans23=request.POST.get("ans23")
    ans24=request.POST.get("ans24")
    ans25=request.POST.get("ans25")
    ans26=request.POST.get("ans26")
    ans27=request.POST.get("ans27")
    ans28=request.POST.get("ans28")
    ans29=request.POST.get("ans29")
    ans30=request.POST.get("ans30")
    ans31=request.POST.get("ans31")
    ans32=request.POST.get("ans32")
    ans33=request.POST.get("ans33")
    ans34=request.POST.get("ans34")
    ans35=request.POST.get("ans35")
    ans36=request.POST.get("ans36")
    ans37=request.POST.get("ans37")
    ans38=request.POST.get("ans38")
    ans39=request.POST.get("ans39")
    ans40=request.POST.get("ans40")


    # d={"idno":idno,"que1":que1,"que2":que2,"que3":que3,"que4":que4,"que5":que5,"que6":que6,"que7":que7,"que8":que8,"que9":que9,"que10":que10,
     #  "ans1":ans1,"ans2":ans2,"ans3":ans3,"ans4":ans4,"ans5":ans5,"ans6":ans6,"ans7":ans7,"ans8":ans8,"ans9":ans9,"ans10":ans10,
      # "ans11":ans11,"ans12":ans12,"ans13":ans13,"ans14":ans14,"ans15":ans15,"ans16":ans16,"ans17":ans17,"ans18":ans18,"ans19":ans19,"ans20":ans20,
       #"ans21":ans21,"ans22":ans22,"ans23":ans23,"ans24":ans24,"ans25":ans25,"ans26":ans26,"ans27":ans27,"ans28":ans28,"ans29":ans29,"ans30":ans30,
       #"ans31":ans31,"ans32":ans32,"ans33":ans33,"ans34":ans34,"ans35":ans35,"ans36":ans36,"ans37":ans37,"ans38":ans38,"ans39":ans39,"ans40":ans40,
       #}"""
    Exam2(idno=idno, que1=que1, que2=que2, que3=que3, que4=que4, que5=que5, que6=que6, que7=que7, que8=que8, que9=que9,que10=que10,
      ans1=ans1, ans2=ans2, ans3=ans3, ans4=ans4, ans5=ans5, ans6=ans6, ans7=ans7, ans8=ans8, ans9=ans9,
      ans10=ans10,
      ans11=ans11, ans12=ans12, ans13=ans13, ans14=ans14, ans15=ans15, ans16=ans16, ans17=ans17, ans18=ans18,
      ans19=ans19, ans20=ans20,
      ans21=ans21, ans22=ans22, ans23=ans23, ans24=ans24, ans25=ans25, ans26=ans26, ans27=ans27, ans28=ans28,
      ans29=ans29, ans30=ans30,
      ans31=ans31, ans32=ans32, ans33=ans33, ans34=ans34, ans35=ans35, ans36=ans36, ans37=ans37, ans38=ans38,
      ans39=ans39, ans40=ans40).save()
    return render(request, "Exam4.html")


def exam3(request):
    qs=Exam2.objects.all()
    return render(request,"Exam3.html",{"data":qs})


def exam4(request):
    idno=request.POST.get("idno")
    que1=request.POST.get("que1")
    que2=request.POST.get("que2")
    que3=request.POST.get("que3")
    que4=request.POST.get("que4")
    que5=request.POST.get("que5")
    que6=request.POST.get("que6")
    que7=request.POST.get("que7")
    que8=request.POST.get("que8")
    que9=request.POST.get("que9")
    que10=request.POST.get("que10")
    Exam3(idno=idno,que1=que1,que2=que2,que3=que3,que4=que4,que5=que5,que6=que6,que7=que7,que8=que8,que9=que9,que10=que10).save()
    return render(request,"Exam4.html")

def exam6(request):
    qs = Exam3.objects.all()
    qs1=Answer.objects.all()
    return render(request,"Exam5.html",{"data":qs,"data1":qs1})

def exam5(request):
    return render(request,"Exam6.html")

def answer(request):
    answer1=request.POST.get("answer1")
    answer2=request.POST.get("answer2")
    answer3=request.POST.get("answer3")
    answer4=request.POST.get("answer4")
    answer5=request.POST.get("answer5")
    answer6=request.POST.get("answer6")
    answer7=request.POST.get("answer7")
    answer8=request.POST.get("answer8")
    answer9=request.POST.get("answer9")
    answer10=request.POST.get("answer10")
    Answer(answer1=answer1,answer2=answer2,answer3=answer3,answer4=answer4,answer5=answer5,answer6=answer6,answer7=answer7,answer8=answer8,answer9=answer9,answer10=answer10).save()
    return render(request,"Exam4.html")


def home(request):
    return render(request,"home2.html")


def search(request):
    y = request.GET['idno']
    recs = Exam3.objects.filter(idno=y)
    recd=Answer.objects.all()
    return render(request, "student.html",{"recs":recs,"recd":recd})


def home1(request):
    return render(request, "home3.html")


def search1(request):
    y = request.GET['idno']
    recs = Exam3.objects.filter(idno=y)
    qr = Student.objects.filter(idno=y)
    recd = Answer.objects.all()
    recs1=Exam3.objects.all()
    recd1=Answer.objects.all()
    return render(request, "student1.html", {"recs": recs, "recd": recd,"qr":qr,"recs1":recs1,"recd1":recd1})






"""class Update(UpdateView):
    model = Exam2
    template_name = "update12.html"
    fields = ["idno", "que1", "que2", "que3", "que4", "que5", "que6", "que7", "que8", "que9", "que10", 
    "ans1", "ans2","ans3", "ans4",
              "ans5", "ans6", "ans7", "ans8", "ans9", "ans10", "ans11", "ans12", "ans13", "ans14", "ans15", "ans16",
              "ans17", "ans18","ans19", "ans20", "ans21", "ans22", "ans23", "ans24", "ans25", "ans26", "ans27", "ans28",
              "ans29", "ans30", "ans31","ans32", "ans33", "ans34", "ans35", "ans36", "ans37", "ans38", "ans39", "ans40"]
    success_url = "/show/"""


class Show12(CreateView):
    model =Exam2
    template_name = "index12.html"
    fields = ["idno"]
    success_url = "/Ram1/"

class Up(UpdateView):
    model = Exam2
    template_name = "Update12.html"
    fields = ["idno",
              "que1",
              "ans1", "ans2", "ans3", "ans4",
              "que2",
              "ans5", "ans6", "ans7", "ans8",
              "que3",
              "ans9", "ans10", "ans11", "ans12",
              "que4",
              "ans13", "ans14", "ans15", "ans16",
              "que5",
              "ans17", "ans18", "ans19", "ans20",
              "que6",
              "ans21", "ans22", "ans23", "ans24"
              ,"que7",
              "ans25", "ans26", "ans27", "ans28"
              ,"que8",
              "ans29", "ans30", "ans31", "ans32",
              "que9",
              "ans33", "ans34", "ans35", "ans36",
              "que10",
              "ans37", "ans38", "ans39", "ans40"
              ]
    success_url = "/Ram1/"

class Del(DeleteView):
    model = Exam2
    template_name = "delete12.html"
    fields = ["idno",]
    success_url = "/Ram1/"



