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
from django.views.generic import TemplateView
from Radha18 import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import urlpatterns

from app import views

urlpatterns += staticfiles_urlpatterns()
from django.views.generic import TemplateView,ListView,DeleteView,DetailView
from app.models import Std
from app.models import Std1
from app.models import Chart



from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
     path("",TemplateView.as_view(template_name="Main.html"),name="main"),
    path("about/",TemplateView.as_view(template_name="about.html"),name="about"),
    path("information/",TemplateView.as_view(template_name="informaction.html"),name="informaction"),
    path("", TemplateView.as_view(template_name="index1.html"), name="index1"),
    path("index2", TemplateView.as_view(template_name="index3.html"), name="index3"),
    path("index3", TemplateView.as_view(template_name="index4.html"), name="index4"),
    path("Teacher/", TemplateView.as_view(template_name="Teacher.html"), name="Teacher"),

    path("index/",views.index, name="index"),
    path("send/", views.send),
    path("show/", views.show, name="show"),

    path("AllDet/",TemplateView.as_view(template_name="Login.html"),name="AllDet"),
    path("login", views.login, name="login"),
    path("Det/", TemplateView.as_view(template_name="Question.html"), name="Det"),
    path("AllDetailes/", TemplateView.as_view(template_name="AllDetails.html"), name="AllDetailes"),
    path("chart/", views.chart, name="chart"),
    path("Tea/", views.Tea),
    path("TeaDet/", TemplateView.as_view(template_name="TeacherLogin.html"), name="TeaDet"),
    path("Tlogin", views.tlogin, name="Tlogin"),

    path('index4/', TemplateView.as_view(template_name="StudentQuection.html")),
    path('viewall/', views.Detail.as_view(), name='viewall'),
    path('index4/', TemplateView.as_view(template_name="TeacherQuection.html")),
    path('Map/', TemplateView.as_view(template_name="Map.html"),name="Map"),
    path('ramayanam/', TemplateView.as_view(template_name="ramayanam.html"),name="ramayanam"),
    path('science/', TemplateView.as_view(template_name="science.html"),name="science"),
    path('Free/', TemplateView.as_view(template_name="Free.html"),name="Free"),
    path('Free1/', TemplateView.as_view(template_name="Free1.html"),name="Free1"),
    path('Free2/', TemplateView.as_view(template_name="Free2.html"),name="Free2"),
    path('Free3/', TemplateView.as_view(template_name="Free3.html"),name="Free3"),
    path('all/', views.TeaDetail.as_view(), name='all'),

    path('index6/',views.Show.as_view(), name="Radha"),
    path('Ram/', ListView.as_view(template_name="Home.html", model=Std), name="ram"),
    path('update<int:pk>/', views.Update.as_view(), name="up"),
    path('delete<int:pk>/', views.Delete.as_view()),
    path('logout/', views.logout, name="logout"),

    path('rmd/', views.exam1, name="rmd"),
    path('exam2/', views.exam2, name="exam2"),
    path('exam3/', views.exam3, name="exam3"),
    path('exam4/', views.exam4, name="exam4"),
    path('ALLD/', TemplateView.as_view(template_name="Exam5.html"), name="ALLD"),
    path('exam5/', views.exam5, name="exam5"),
    path('exam6/', views.exam6, name="exam6"),
    path('answer/', views.answer, name="answer"),

    path('home/', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('tem/', TemplateView.as_view(template_name="student1.html"), name="tem"),
    path('home1/', views.home1, name='home1'),
    path('search1/', views.search1, name='search1'),
    path('index16/', views.Show12.as_view(), name="Radha12"),
    path('Ram1/', ListView.as_view(template_name="Home12.html", model=Exam2), name="Ram1"),
    path('up1<int:pk>/', views.Up.as_view(), name="up1"),
    path('del<int:pk>/', views.Del.as_view()),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

