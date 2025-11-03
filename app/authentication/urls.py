from . import views
from django_distill import distill_path

urlpatterns = [
    distill_path('login/', views.login, name='login'),
    distill_path('register/', views.register, name='register'),
]