from django.shortcuts import render
from .models import WebsiteCommon
from .models import HeaderSection
from .models import Menu
from .models import AboutSection
from .models import Projects
from .models import Contact
from .models import FooterIcon, Subscription

from django.contrib import messages

# Create your views here.
def index(requst):
    context = {}
    context["common"] = WebsiteCommon.objects.last()
    context["header"] = HeaderSection.objects.last()
    context["menu_list"] = Menu.objects.all()
    context["about"] = AboutSection.objects.last()
    context["project_list"] = Projects.objects.all()[:3]
    context["contact_list"] = Contact.objects.all()
    context["footer_list"] = FooterIcon.objects.all()

    if requst.method == "POST":
        email = requst.POST.get("email")
        Subscription.objects.create(
            email=email
        )
        messages.info(
            requst,
            f"bu {email} Eelave olundu. Bizi izledyinz uhcun teshekkur edirik"
        )

    return render(requst, "index.html", context)
