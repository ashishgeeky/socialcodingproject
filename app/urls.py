
from django.urls import path, re_path
from app import views

urlpatterns = [


    # The home page
    path('', views.index, name='home'),
    path('statewise', views.statewise, name='statewise'),
    path('infectedstate', views.infectedstate, name='infectedstate'),
    path('recoveredstate', views.recoveredstate, name='recoveredstate'),
    path('deathstate', views.deathstate, name='deathstate'),
    path('importantlinks', views.importantlinks, name='importantlinks'),
    path('prediction/<str:city_name>', views.prediction, name='prediction'),
    path('predictionall', views.predictionall, name='predictionall'),

]
