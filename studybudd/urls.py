"""
URL configuration for studybudd project.

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
from django.urls import path,include 


from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('base.urls')),
    path('logout/', include("base.urls")),
    path('login/',include('base.urls')),
    path('register/',include('base.urls')),
    path('room/',include("base.urls")),
    path('create-room/',include("base.urls")),
    path('update-room/',include("base.urls")),
    path('delete-room/',include("base.urls")),
    path('delete-message/',include("base.urls")),
    path('home/',include("base.urls")),
    ]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)