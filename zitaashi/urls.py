"""
URL configuration for zitaashi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from cms.views import HomePageView, ZitaashiStudioView
from zitaashi import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('cms.urls')),
    path('', HomePageView.as_view(template_name='index.html')),
    path('studio/', ZitaashiStudioView.as_view(template_name='zitaashi_studio_new.html')),
]

admin.sites.AdminSite.site_header = 'Zitaashi Admin'
admin.sites.AdminSite.site_title = 'Zitaashi Admin'
admin.sites.AdminSite.index_title = 'Zitaashi administration'

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
