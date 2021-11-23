from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
# Create your models here.

class Place(models.Model):
  name = models.CharField(max_length=100)
  location = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  date = models.DateField('Start Date')
  end_date =  models.DateField('End Date')
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('places_detail', kwargs={'place_id': self.id})


class Photo(models.Model):
  url = models.CharField(max_length=250)
  place = models.OneToOneField(Place, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for place_id: {self.place_id} @{self.url}"
