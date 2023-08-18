from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView

from .models import Finch, Tag
from .forms import FeedingForm

# finches = [
#     {'species': 'House Finch', 'color': 'red', 'description': 'The house finch is a bird in the finch family Fringillidae. It is native to western North America and has been introduced to the eastern half of the continent and Hawaii.', 'spotted': 2 },
#     {'species': 'European Gold Finch', 'color': 'Gold', 'description': 'The European goldfinch or simply the goldfinch is a small passerine bird in the finch family that is native to Europe, North Africa and western and central Asia.', 'spotted': 4 },
#     {'species': 'Desert Finch', 'color': 'Sandy Brown', 'description': 'The desert finch, sometimes called Lichtensteins desert finch, is a large brown true finch found in southern Eurasia.', 'spotted': 2 },
# ]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {
        'finches': finches
    })

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    feeding_form = FeedingForm()
    return render(request, 'finches/detail.html', {
        'finch': finch, 'feeding_form': feeding_form
    })

class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'


class FinchUpdate(UpdateView):
    model = Finch
    fields = ['color', 'description', 'spotted']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches'


def add_feeding(request, finch_id):
  
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the finch_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.finch_id = finch_id
    new_feeding.save()
  return redirect('detail', finch_id=finch_id)

class TagList(ListView):
    model = Tag

class TagDetail(DetailView):
    model = Tag

class TagCreate(CreateView):
    model = Tag
    fields = '__all__'

class TagUpdate(UpdateView):
    model = Tag
    fields = '__all__'

class TagDelete(DeleteView):
    model = Tag
    success_url = '/tags'