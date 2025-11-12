"""
URL configuration for configs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('app.dashboards.urls')),  # include your app URLs
#     path('authentication/', include('app.authentication.urls'))
# ]
from django_distill import distill_path
from app.dashboards import views as dash_views
from app.ui import views as ui_views
from app.authentication import views as auth_views
from app.icon_tabler import views as icon_views
def no_params():
    return None
handler404 = 'app.dashboards.views.custom_404'
urlpatterns = [
    # Dashboards
    path('admin/', admin.site.urls),
    distill_path('', dash_views.index, name='index', distill_func=no_params),
    distill_path('ui-buttons/', ui_views.uibutton, name='ui-buttons', distill_func=no_params),
    distill_path('ui-card/', ui_views.uicard, name='ui-card', distill_func=no_params),
    distill_path('ui-alerts/', ui_views.uialerts, name='ui-alerts', distill_func=no_params),
    distill_path('icon-tabler/', icon_views.icontabler, name='icon-tabler', distill_func=no_params),
    distill_path('ui-forms/', ui_views.uiforms, name='ui-forms', distill_func=no_params),
    distill_path('ui-typography/', ui_views.uitypography, name='ui-typography', distill_func=no_params),
    distill_path('sample-page/', dash_views.samplepage, name="sample-page", distill_func=no_params),

    # Authentication
    distill_path('login/', auth_views.login, name='login', distill_func=no_params),
    distill_path('register/', auth_views.register, name='register', distill_func=no_params),
]
