# st/views.py

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import  reverse_lazy
from django.views.generic.edit import UpdateView,DeleteView,CreateView

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
    fields = ['Latittude','Longitude','S_ID','Date','Age','Fur','Location','S_location',
            'Run','Chase','Climb','Eat','Forage','Other_a','Kuks','Quaas','Moans',
            'T_flag','T_twitch','Approach','Indifferent','Run_from']
    template_name = 'st/update.html'
    success_url = '/st/sightings'

    def post(self, request, pk):
        if 'confirm_delete' in self.request.POST:
            post_delete = Squirrel.objects.get(pk=pk)
            post_delete.delete()

        return render(request, 'st/index.html', {
        'all_squirrel_sightings': Squirrel.objects.all(),
    })

    def form_valid(self, form):
        if 'confirm_post' in self.request.POST:
            form.instance.user = self.request.user
        return super(update, self).form_valid(form)
# a view to create a new sighting
class create(CreateView):
    model = Squirrel
    fields = ['Latittude','Longitude','S_ID','Date','Age','Fur','Location','S_location',
            'Run','Chase','Climb','Eat','Forage','Other_a','Kuks','Quaas','Moans',
            'T_flag','T_twitch','Approach','Indifferent','Run_from']
    template_name = 'st/create.html'

    def get_success_url(self):
        return reverse_lazy('st:index')

# a view to delete a sighting
class delete(DeleteView):
    model = Squirrel
    success_url = reverse_lazy('index')

# a view with general stats about the sighting


