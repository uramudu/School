from django.db import models
class Student(models.Model):
    idno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    surname=models.CharField(max_length=30)
    father=models.CharField(max_length=30)
    mother=models.CharField(max_length=30)
    date=models.CharField(max_length=30)
    gen=models.CharField(max_length=30)
    phone=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    section=models.CharField(max_length=30)
    image = models.FileField(upload_to='profile_pics/', blank=True)
class Chart(models.Model):
    num=models.CharField(max_length=30)
    quection=models.CharField(max_length=1000)
class Teacher(models.Model):
    name = models.CharField(max_length=30)
    date = models.CharField(max_length=30)
    gen = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    sub=models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
class Chart1(models.Model):
    num=models.CharField(max_length=30)
    Answer=models.CharField(max_length=1000)
class Std(models.Model):
    num=models.IntegerField(primary_key=True)
    Answer=models.CharField(max_length=30)






