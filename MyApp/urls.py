from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.PersonListView, name='person_changelist'),
    path('add/', views.PersonCreateView, name='person_add'),
    path('<int:pk>/', views.PersonUpdateView, name='person_change'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
]