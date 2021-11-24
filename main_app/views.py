from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Place,  Photo
import uuid
import boto3
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'cronaldo'

# Define the home view





def about(request):
  return render(request, 'about.html')


@login_required
def places_index(request):
  places = Place.objects.filter(user=request.user)
  return render(request, 'places/index.html', {'places': places})


@login_required
def places_detail(request, place_id):
  place = Place.objects.get(id=place_id)
  return render(request, 'places/detail.html', { 'place': place })


@login_required
def add_photo(request, place_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Photo(url=url, place_id=place_id)
      place_photo = Photo.objects.filter(place_id=place_id)
      if place_photo.first():
        place_photo.first().delete()
      photo.save()
    except Exception as err:
      print('An error occurred uploading file to S3: %s' % err)
  return redirect('places_detail', place_id=place_id)

  
def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('cats_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)


class Home(LoginView):
  template_name = 'home.html'


class PlaceCreate(LoginRequiredMixin, CreateView):
  model = Place
  fields = ['name', 'location', 'description', 'date', 'end_date']
  success_url = '/places/'

  def form_valid(self, form):
    form.instance.user = self.request.user  
    return super().form_valid(form)


class PlaceUpdate(LoginRequiredMixin, UpdateView):
  model = Place
  fields = '__all__'

class PlaceDelete(LoginRequiredMixin, DeleteView):
  model = Place
  success_url = '/places/'
