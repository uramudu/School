"""Radha1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Radha1 import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import urlpatterns
urlpatterns += staticfiles_urlpatterns()
from django.views.generic import TemplateView,ListView,DeleteView,DetailView
from app.models import Std
from app.models import Chart

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",TemplateView.as_view(template_name="index1.html"),name="index1"),
    path("index2",TemplateView.as_view(template_name="index3.html"),name="index3"),
    path("index3",TemplateView.as_view(template_name="index4.html"),name="index4"),
    path("Teacher/", TemplateView.as_view(template_name="Teacher.html"), name="Teacher"),
    path("index/",views.index,name="index"),
    path("send/",views.send),
    path("show/",views.show,name="show"),
    #path("all/",views.Allstudent.as_view(),name="all"),
    #path('oneempdetails<int:pk>/',views.OneEmployee.as_view(),name='oneemp'),
    path("AllDet/",TemplateView.as_view(template_name="Login.html"),name="AllDet"),
    path("login",views.login,name="login"),
    path("Det/",TemplateView.as_view(template_name="Question.html"), name="Det"),
    path("AllDetailes/",TemplateView.as_view(template_name="AllDetails.html"),name="AllDetailes"),
    path("chart/",views.chart,name="chart"),
    path("Tea/",views.Tea),
    path("TeaDet/",TemplateView.as_view(template_name="TeacherLogin.html"),name="TeaDet"),
    path("Tlogin",views.tlogin,name="Tlogin"),
   # path("StudentQuection/",TemplateView.as_view(template_name="StudentQuection.html"),name="StudentQuection"),
    #path("details/",views.details,name="details"),
    #path("details<int:pk>/",views.Detail.as_view(),name="details"),
    path('index4/', TemplateView.as_view(template_name="StudentQuection.html")),
    path('viewall/', views.Detail.as_view(), name='viewall'),
    path('index4/', TemplateView.as_view(template_name="TeacherQuection.html")),
    path('all/', views.TeaDetail.as_view(), name='all'),
    #path('onedetails<int:pk>/',DetailView.as_view(template_name="StudentQuection.html",model=Chart), name='oneemp'),
    path('index6/',views.Show.as_view(),name="Radha"),
    path('Ram/',ListView.as_view(template_name="Home.html", model=Std), name="ram"),
    path('update<int:pk>/',views.Update.as_view(),name="up"),
    path('delete<int:pk>/',views.Delete.as_view()),
    path('logout/',views.logout,name="logout"),
    #path('Tlogout/',views.tlogout,name="Tlogout"),
    #path('Radha1/',views.TeaShow.as_view(),name="Radha1"),
    #path('Tea1/',ListView.as_view(template_name="TeaherHome.html", model=Chart), name="Tea1"),
    #path('Teaup<int:pk>/',views.TeaUp.as_view()),
    #path('Teadel<int:pk>/',views.TeaDel.as_view())



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
