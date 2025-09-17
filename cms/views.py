import threading

from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from rest_framework import status
from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework.views import APIView

from cms.models import Testimonial, ContactForm, OurClient, RecentWork, ZitaashiStudio
from zitaashi import settings


# Create your views here.

def send_mail_template_async(subject, template_name, context, recipient_list, fail_silently=False):
    """Send HTML + text mail asynchronously."""
    html_content = render_to_string(template_name, context)
    text_content = render_to_string(template_name, context)

    email = EmailMultiAlternatives(
        subject=subject,
        body=text_content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=recipient_list,
    )
    email.attach_alternative(html_content, "text/html")
    email.send(fail_silently=fail_silently)


class ContactFormSubmitView(APIView):
    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        if not (name and email and subject and message):
            return Response(
                {"status": "error", "message": "All fields are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        ContactForm.objects.create(
            name=name, email=email, subject=subject, phone_number=phone_number, message=message,
        )

        try:
            threading.Thread(
                target=send_mail_template_async,
                args=(
                    f"New Contact Form: {subject}",
                    "emails/contact_admin.html",
                    {"name": name, "email": email, "phone_number": phone_number, "message": message},
                    [settings.CONTACT_EMAIL],
                ),
            ).start()

            threading.Thread(
                target=send_mail_template_async,
                args=(
                    "Zitaashi - Thank you for contacting us. We received your message",
                    "emails/contact_user.html",
                    {"name": name, "message": message},
                    [email],
                ),
                kwargs={"fail_silently": True},
            ).start()
        except Exception as e:
            return Response(
                {"status": "error", "message": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response({"status": "success"}, status=status.HTTP_200_OK)


class HomePageView(TemplateView):
    template_name = '/'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['testimonials'] = Testimonial.objects.all()
        context['our_clients'] = OurClient.objects.all()
        context['recent_works'] = RecentWork.objects.all()
        return context


class ZitaashiStudioView(TemplateView):
    template_name = 'zitaashi_studio_new.html'

    def get_context_data(self, **kwargs):
        context = super(ZitaashiStudioView, self).get_context_data(**kwargs)
        context['banner_image'] = ZitaashiStudio.objects.filter(image_type='banner').last()
        context['sub_banner'] = ZitaashiStudio.objects.filter(image_type='sub_banner').order_by('-id')[:2]
        context['studio_tour'] = ZitaashiStudio.objects.filter(image_type='studio_tour').order_by('-id')[:3]
        return context