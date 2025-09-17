from django.db import models

# Create your models here.


class ContactForm(models.Model):
    CONTACT_TYPE = [
        ('contact', 'Contact'),
        ('consultancy', 'Consultancy')
    ]
    date_created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=15, default=0)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    contact_type = models.CharField(max_length=20, choices=CONTACT_TYPE, default='contact')
    message = models.TextField()


class Testimonial(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=250)
    designation = models.CharField(max_length=250)
    feedback = models.TextField()


class OurClient(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    logo = models.ImageField(upload_to='client')
    website_link = models.URLField(null=True, blank=True)


class RecentWork(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    video_code = models.CharField(max_length=200, null=True, blank=True)


class ZitaashiStudio(models.Model):
    IMAGE_TYPE = [
        ('banner', 'Banner'),
        ('sub_banner', 'Sub Banner'),
        ('studio_tour', 'Studio Tour')
    ]
    date_created = models.DateTimeField(auto_now_add=True)
    heading = models.CharField(max_length=250)
    image_type = models.CharField(max_length=20, choices=IMAGE_TYPE)
    image = models.ImageField(upload_to='studio')

    def __str__(self):
        return str(self.id)

