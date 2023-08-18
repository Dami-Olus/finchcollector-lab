from django.shortcuts import render

from .models import Finch

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
    return render(request, 'finches/detail.html', {
        'finch': finch
    })
