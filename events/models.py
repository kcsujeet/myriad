from multiprocessing.synchronize import Event
import datetime
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class DateTimeModel(models.Model):
	created_at = models.DateTimeField(
		auto_now_add=True, auto_now=False, null=True, blank=True)
	updated_at = models.DateTimeField(
		auto_now_add=False, auto_now=True, null=True, blank=True)
	deleted_at = models.DateTimeField(null=True, blank=True)

	class Meta:
		abstract = True


class UserModel(DateTimeModel):
	created_by = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)

	class Meta:
		abstract = True

class Event(UserModel):
    event_name = models.CharField(max_length=100, null = True, blank =True)
    description = models.TextField(max_length=4000, null=True, blank=True)
    date_time = models.DateTimeField(default = datetime.datetime.now,null=True,blank=True)
    venue = models.CharField(max_length= 100, null = True, blank = True)
    venue_url = models.URLField(null=True, blank = True)
    signup_form_code =  models.TextField (max_length=500, null=True, blank=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.event_name