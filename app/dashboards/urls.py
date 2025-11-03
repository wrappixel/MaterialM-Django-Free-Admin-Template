from django.urls import path
from . import views
from django_distill import distill_path


urlpatterns = [
    path('', views.index, name='index'),  # homepage
    path('sample-page', views.samplepage, name="sample-page")
]
