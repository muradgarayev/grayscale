from django.db import models


# Create your models here.
class WebsiteCommon(models.Model):
    brand = models.CharField(max_length=255)
    copyright_text = models.CharField(max_length=255)
    subscribe_text = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.brand)


class HeaderSection(models.Model):
    backgroud_image = models.ImageField(upload_to="header/")
    main_title = models.CharField(max_length=255)
    sub_title = models.TextField()
    button_text = models.CharField(max_length=255, null=True, blank=True)
    button_link = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.main_title)


class Menu(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    order = models.IntegerField(default=0)

    def __str__(self):
        return "{}".format(self.name)


class AboutSection(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    picture = models.ImageField(upload_to="about/")

    def __str__(self):
        return "{}".format(self.title)


class Projects(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    picture = models.ImageField(upload_to="projects/")


class Contact(models.Model):
    icon = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return "{}".format(self.title)


class FooterIcon(models.Model):
    link = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.name)


class Subscription(models.Model):
    email = models.EmailField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.email)
