from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Courses(models.Model):
    name = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='lessons/%y/%m', max_length=225, null=True, blank=True)

    class Meta:
        abstract = True


class Cares(models.Model):
    name = models.CharField(max_length=225)


class Lessons(BaseModel):
    name = models.CharField(max_length=225)
    description = models.CharField(max_length=225)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='lessons')
    cares = models.ManyToManyField('Cares', related_name='lessons', blank=True, null=True)


class Tags(models.Model):
    name = models.CharField(max_length=225)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    lessons = models.ForeignKey(Lessons, on_delete=models.SET_NULL, related_name='tags', null=True)


class Users(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=225)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
