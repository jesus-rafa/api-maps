from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = [
    path('admin/', admin.site.urls),

    # apps locales
    re_path('', include('applications.users.urls')),
    re_path('', include('applications.home.urls')),
    re_path('', include('applications.poligonos.urls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

