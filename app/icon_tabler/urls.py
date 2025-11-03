
from django.urls import path
from . import views

urlpatterns = [
    path('icon-tabler/', views.icontabler, name='icon-tabler'),
]