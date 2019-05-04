"""portafolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, re_path
from django.conf import settings
from core import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('portafolio/', views.portafolio, name='portafolio'),
    path('portafolio/<id>/', views.project, name='project'),
    path('portafolio/agregar', views.addproject, name='addproject'),
    path('browser/', views.browser, name='browser'),
    re_path(r'saludo/(?P<name>\w*)', views.saludo, name='saludo'),
    path('admin/', admin.site.urls),
]

#si el debug de setting es true agrega las rutas
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

