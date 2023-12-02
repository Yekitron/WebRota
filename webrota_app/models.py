from django.db import models


# Create your models here.
# models.py
from datetime import datetime

class Shifting(models.Model):
    choices_shift = [('Day','Day'),('Night','Night'),]
    choices_user = [('User_A','User_A'),('User_B','User_B'),('User_C','User_C'),('User_D','User_D')]
    user = models.CharField(max_length=100, choices=choices_user, default='',help_text='Select user')
    date = models.DateField()#input_formats=['%Y-%m-%d']
    shift = models.CharField(max_length=5, choices= choices_shift, default='', help_text='Select the shift time: Day or Night')




print(Shifting.objects.all())