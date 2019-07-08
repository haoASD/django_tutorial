from django.contrib import admin
from django.urls import path,include
from django.views.generic import RedirectView

from . import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('quickstart.urls')),
]


from django.conf import settings
from django.conf.urls.static import static
"""
Establece el path a la carpeta static
"""
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)