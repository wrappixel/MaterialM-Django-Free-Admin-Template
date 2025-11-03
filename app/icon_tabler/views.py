from web_project.helpers.template_heplers import TemplateHelper


def icontabler(request):
    # return render(request, "icon-tabler.html")
    return TemplateHelper.render(request, "icon-tabler.html",page_title="Icon Tabler")
