from django.shortcuts import render
from django.http import HttpResponse
import random
import string

# Create your views here.

def home (request):
  return render(request, 'generator/home.html')


def about (request):
  return render(request, 'generator/about.html')


def password (request):

  length = int(request.GET.get('length', 25))
  characters = list(string.ascii_lowercase)
  passwordout = ''


  if request.GET.get('uppercase'):
    capitals = list(string.ascii_uppercase)
    characters.extend(capitals)

  if request.GET.get('numbers'):
    digits = list(string.digits)
    characters.extend(digits)

  if request.GET.get('special'):
    symbols = list(string.punctuation)
    characters.extend(symbols)

  for x in range(length):
    passwordout += random.choice(characters)

  return render(request, 'generator/password.html', {'password':passwordout})