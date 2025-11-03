# helpers/template_helper.py

from django.conf import settings
from django.shortcuts import render
from django.utils.safestring import mark_safe


class TemplateHelper:

    PROJECT_NAME = "MaterailM Free Bootstrap Admin Template by WrapPixel"

    @staticmethod
    def render(request, template_path, context=None, page_title=None):
        """
        Wrapper around Django render() to inject project-wide defaults.
        """
        if context is None:
            context = {}

        # Add Project Name
        context["project_name"] = TemplateHelper.PROJECT_NAME

        # Add Page Title
        context["page_title"] = page_title or TemplateHelper._auto_title_from_path(template_path)

        # Add Active Sidebar Detection
        context["active_sidebar"] = TemplateHelper._get_active_sidebar(request)

        return render(request, template_path, context)

    @staticmethod
    def _auto_title_from_path(template_path):
        # Example: "dashboards/index.html" -> "Index"
        name = template_path.split("/")[-1].replace(".html", "")
        return name.replace("-", " ").title()

    @staticmethod
    def _get_active_sidebar(request):
        # Returns the current request path (used in HTML to highlight active menu)
        return request.path

      # Get theme variables by scope
    def get_theme_variables(scope):
        return settings.THEME_VARIABLES[scope]
