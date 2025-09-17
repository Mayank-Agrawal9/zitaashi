from django.urls import path

from cms.views import ContactFormSubmitView

urlpatterns = [
    path("contact-submit/", ContactFormSubmitView.as_view(), name="contact_form_submit"),
]