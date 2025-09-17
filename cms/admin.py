from django.contrib import admin

from cms.models import ContactForm, Testimonial, OurClient, RecentWork, ZitaashiStudio


# Register your models here.


@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['id', 'date_created', 'name', 'email', 'subject']


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['id', 'date_created', 'name', 'designation', 'feedback']


@admin.register(OurClient)
class OurClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'date_created', 'logo', 'website_link']


@admin.register(RecentWork)
class RecentWorkAdmin(admin.ModelAdmin):
    list_display = ['id', 'date_created', 'video_code']


@admin.register(ZitaashiStudio)
class ZitaashiStudioAdmin(admin.ModelAdmin):
    list_display = ['id', 'date_created', 'heading', 'image_type']