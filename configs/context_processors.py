from django.conf import settings
from web_project.helpers.template_heplers import TemplateHelper
def my_setting(request):
    return {'MY_SETTING': settings}


# Add the 'ENVIRONMENT' setting to the template context
def environment(request):
    return {'ENVIRONMENT': settings.ENVIRONMENT}


def theme_variables(request):
    return {
        'DEBUG': settings.DEBUG,                  # True/False
        'THEME_BASE_URL': TemplateHelper.get_theme_variables('route_perfix'),
        # getattr(settings, 'route_perfix', '/free/product-name')
    }