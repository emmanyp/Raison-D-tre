from django.shortcuts import render


# Define the home view


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')


def places_index(request):
  return render(request, 'places/index.html', {'places': places})

class Place:
  def __init__(self, name, location, description, start_date, end_date):
    self.name = name
    self.location = location
    self.description = description
    self.start_date = start_date
    self.end_date = end_date

places = [
  Place('dear Han', 'NYC NY', 'cafe', 'april 2020', 'Aug 2021' ),
  Place('dear Han', 'NYC NY', 'cafe', 'april 2020', 'Aug 2021' ),
  Place('dear Han', 'NYC NY', 'cafe', 'april 2020', 'Aug 2021' ),
]