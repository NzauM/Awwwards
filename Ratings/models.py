from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    profile_pic = models.ImageField(upload_to='pictures/')
    bio = models.TextField(max_length=1000)
    info = models.TextField(max_length=5000)
    
class Projects(models.Model):
    '''
    Class for instantiating all projects objects
    '''
    title = models.CharField(max_length=500)
    description=models.TextField(max_length=2000)
    link=models.URLField()
    image=models.ImageField(upload_to='pictures/')

    def save_project(self):
        '''
        Function for saving a project
        '''
        self.save()

    @classmethod
    def all_projects(cls):
        '''
        Function for getting all projects
        '''
        all_projects = cls.objects.all()
        return all_projects