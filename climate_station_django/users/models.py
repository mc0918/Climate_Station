from django.db import models

# Create your models here.
class Users(models.Model):
    user_name = models.CharField(max_length=200)
    join_date = models.DateTimeField('date joined')

class Saved_Data(models.Model):
    Record = models.IntegerField(default=0)
    Record_Date = models.CharField(max_length=200)
