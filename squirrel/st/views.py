from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import UpdateView

from .models import Squirrel

# a view that shows a map that display the location of the squirrel sightings on openstreet map



# a veiw that lists all squirrel sightings with links to edit and add sightings
def index(request):
    all_squirrel_sightings = Squirrel.objects.all()
    context = {
        'all_squirrel_sightings': all_squirrel_sightings,
    }
    return render(request, 'st/index.html', context)

# a view to update a particular sighting
class update(UpdateView):
    model = Squirrel
    fields = ['X','Y','S_ID','Shift']
    template_name = 'st/update.html'

    def get_object(self):
        return Squirrel.objects.get(pk=self.request.GET.get('pk'))
#def update(request, sid):
#    sq = get_object_or_404(Squirrel, pk=sid)
#    return render(request, 'st/update.html',{'sq': sq})

# a view to create a new sighting


# a view to delete a sighting


# a view with general stats about the sighting


