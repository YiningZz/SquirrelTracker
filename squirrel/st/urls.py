from django.urls import path
from . import views

app_name = 'st'
urlpatterns = [
    # ex: /st/map
   #  path('map', views.map, name='map'),
    # ex: /st/sightings
    path('sightings', views.index, name='index'),
    # ex: /st/sightings/37F-PM-1014-03
    path('sightings/' + r'^(?P<pk>[A-Z0-9-]+)$',views.update.as_view(), name='update'),
    # ex: /st/sightings/add

    # ex: /st/sightings/37F-PM-1014-03

    # ex: /st/sightings/stats
]

