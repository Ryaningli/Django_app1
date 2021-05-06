from django.db import models


class Class(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=10)
    gender = models.CharField(max_length=1)
    birthday = models.DateField()
    grade = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=10)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=10)
    gender = models.CharField(max_length=1)
    birthday = models.DateField()
    s_class = models.ForeignKey('Class', on_delete=models.CASCADE)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    fraction = models.SmallIntegerField()

    def __str__(self):
        return self.name
