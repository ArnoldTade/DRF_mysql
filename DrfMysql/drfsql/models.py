from django.db import models


# Create your models here.
class Student(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    address = models.CharField(max_length=100)


class ImageUpload(models.Model):
    image = models.ImageField(upload_to="img/")
    type = models.CharField(max_length=100)
