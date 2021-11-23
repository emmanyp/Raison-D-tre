from django.db import models
from django.urls import reverse
# Create your models here.

class Place(models.Model):
  name = models.CharField(max_length=100)
  location = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  start_date = models.DateField()
  end_date = models.DateField()

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('places_detail', kwargs={'place_id': self.id})