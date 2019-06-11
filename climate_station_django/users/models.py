from django.db import models
from django.utils import timezone

# Create your models here.
class Users(models.Model):
    user_name = models.CharField(max_length=200)
    join_date = models.DateTimeField('date joined')
    def __str__(self):
        return self.user_name
    def length_joined(self):
        return self.join_date >= timezone.now() - datetime.timedelta(days=1)

class Saved_Data(models.Model):
    Record = models.IntegerField(default=0)
    Record_Date = models.CharField(max_length=200)
    def __str__(self):
        return self.Record