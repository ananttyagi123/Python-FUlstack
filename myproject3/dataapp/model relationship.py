'''In Django, model relationships allow you to define how data in different database tables
(represented by models) is related. There are three main types of relationships:

1. One-to-Many (ForeignKey)
This is the most common type of relationship. 
It means one object can be related to many objects in another model.


from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
Each Book is written by one Author.

An Author can write many Books.

2. Many-to-Many (ManyToManyField)
This is used when each record in one model can be related to many records in another model, and vice versa.

class Student(models.Model):
    name = models.CharField(max_length=100)

class Course(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student)
A Course can have many Students.

A Student can be enrolled in many Courses.

3. One-to-One (OneToOneField)
This relationship means that one object in a model is related to one and only one object in another model.

class User(models.Model):
    username = models.CharField(max_length=100)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
Each User has one Profile.

Each Profile belongs to one User.

on_delete=models.CASCADE means when the related object is deleted, 
also delete the object containing the relationship.

Other options for on_delete: PROTECT, SET_NULL, SET_DEFAULT, DO_NOTHING
'''
