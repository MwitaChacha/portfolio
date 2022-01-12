from django.urls import path
from . import views



urlpatterns=[
   path('',views.index, name='index'),
   path('projects',views.projects,name='projects'),
   path('about',views.about,name='about'),
   path('contact',views.contact,name='contact'),
   path('creative_works',views.creative_works,name='creative_works'),
]