from django.db import models

# Create your models here.
class Users(models.Users):
    user_name = models.CharField(max_length=200)
    join_date = models.DateTimeField('date joined')
