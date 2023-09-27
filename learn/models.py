from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
import os

# Create your models here.
def path_and_rename(instance, filename):
    upload_to='images/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.user.username:
        filename = 'User_profile_Pictures/{}.{}'.format(instance.user.username, ext)
    return os.path.join(upload_to, filename)


class user_profile(models.Model):
    user = models.OneToOneField(User,on_delete= models.CASCADE)
    bio = models.TextField(max_length=150, blank= True)
    profile_pic = models.ImageField(upload_to=path_and_rename, verbose_name='profile_picture', blank=True)

    teacher = 'teacher'
    student = 'student'
    parent = 'parent'
    user_types= [
        (teacher, 'teacher'),
        (student, 'student'),
        (parent, 'parent'),
    ]
    user_type = models.CharField(max_length=10, choices=user_types)

    def __str__(self):
        return self.user.username

class SubscribedUsers(models.Model):
    email = models.EmailField(unique=True, max_length=100)
    created_date = models.DateTimeField('Date created', default=timezone.now)

    def __str__(self):
        return self.email