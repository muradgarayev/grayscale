from django.shortcuts import render
from .models import WebsiteCommon
from .models import HeaderSection
from .models import Menu



# Create your views here.
def index(requst):
    context = {}
    context["common"] = WebsiteCommon.objects.last()
    context["header"] =HeaderSection.objects.last()
    context["menu_list"] =Menu.objects.all()
    return render(requst,"index.html", context)
