from web_project.helpers.template_heplers import TemplateHelper


def uibutton(request):
    return TemplateHelper.render(request, "ui-buttons.html",page_title="UI -buttons")

def uialerts(request):
    # return render(request, "ui-alerts.html")
    return TemplateHelper.render(request, "ui-alerts.html",page_title="UI alerts")

def uicard(request):
    # return render(request, "ui-card.html")
    return TemplateHelper.render(request, "ui-card.html",page_title="UI card")

def uiforms(request):
    # return render(request, "ui-forms.html")
    return TemplateHelper.render(request, "ui-forms.html",page_title="UI forms")

def uitypography(request):
    # return render(request, "ui-typography.html")
    return TemplateHelper.render(request, "ui-typography.html",page_title="UI Typography")
