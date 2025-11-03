from django.urls import path
from . import views


urlpatterns = [
    path('ui-buttons/', views.uibutton, name='ui-buttons'),
    path('ui-card/', views.uicard, name='ui-card'),
    path('ui-alerts/', views.uialerts, name='ui-alerts'),
    path('ui-forms/', views.uiforms, name='ui-forms'),
    path('ui-typography', views.uitypography, name='ui-typography'),
]