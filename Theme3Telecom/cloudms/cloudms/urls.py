"""
URL configuration for cloudms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from msgapp import views as msgviews

urlpatterns = [
    path("admin/", admin.site.urls),
    path("msggate/", include("msgapp.urls")),
    path("tt/", msgviews.homeproc),
    path("", msgviews.pgproc),
    path("playground/", msgviews.homeproc2),
    path("json/", msgviews.homeproc1),
    path('404/', msgviews.not_found),
    path('403/', msgviews.forbidden),
    path('400/', msgviews.bad_request),
    path('redirect/', msgviews.redirect_view),
    path('permanent-redirect/', msgviews.permanent_redirect_view),
    path('streaming/', msgviews.streaming_view),
]
