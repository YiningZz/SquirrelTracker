# st/views.py

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404,redirect
from django.urls import  reverse_lazy
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from django.db.models import Min,Max,Avg,Count

from .models import Squirrel
from .forms import SquirrelForm

# a view that shows a map that display the location of the squirrel sightings on openstreet map
def map(request):
    sightings = Squirrel.objects.all()[0:100] 
    context = {
        'sightings': sightings,
    }
    return render(request, 'st/map.html', context)

#a veiw that lists all squirrel sightings with links to edit and add sightings
def index(request):
    all_squirrel_sightings = Squirrel.objects.all()
    context = {
        'all_squirrel_sightings': all_squirrel_sightings,
    }
    return render(request, 'st/index.html', context)

# a view to update a particular sighting
def update(request, pk):
    sq = Squirrel.objects.get(S_ID=pk)
    if request.method == "POST":
        form = SquirrelForm(request.POST, instance=sq)
        if form.is_valid():
            form.save()
            return redirect(f'/st/sightings/{pk}')
    else:
        form = SquirrelForm(instance=sq)
    context = {
        'form': form,        
    }
    return render(request, 'st/update.html', context)


# a view to create a new sighting
class create(CreateView):
    model = Squirrel
    fields = '__all__'
    template_name = 'st/create.html'

    def get_success_url(self):
        return reverse_lazy('st:index')

# a view to delete a sighting


# a view with general stats about the sighting
def stats(request):
    squirrel_list = Squirrel.objects.all()
    TotalNumber = len(squirrel_list)
    Longitude = squirrel_list.aggregate(min_=Min('Longitude'),
            max_=Max('Longitude'),
            average_=Avg('Longitude'))
    FurCnt = list(squirrel_list.values_list('Fur').annotate(Count('Fur')))
    AgeCnt = list(squirrel_list.values_list('Age').annotate(Count('Age')))
    RunCnt = list(squirrel_list.values_list('Run').annotate(Count('Run')))
    EatCnt = list(squirrel_list.values_list('Eat').annotate(Count('Eat')))
    context = {
        'stats':{'TotalNumber':TotalNumber,
                'Longitude':Longitude,
                'FurCnt':FurCnt,
                'AgeCnt':AgeCnt,
                'RunCnt':RunCnt,
                'EatCnt':EatCnt,},
    }
    return render(request, 'st/stats.html', context)






