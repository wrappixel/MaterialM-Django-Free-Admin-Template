
from django.shortcuts import render
from web_project.helpers.template_heplers import TemplateHelper
# from  import TemplateHelper


def index(request):
    return TemplateHelper.render(request, "index.html", page_title="Dashboard")


def samplepage(request):
    # return render(request, "sample-page.html")
    return TemplateHelper.render(request, "sample-page.html",page_title="Sample Page")

def custom_404(request, exception):
    return render(request, "404.html", status=404)


