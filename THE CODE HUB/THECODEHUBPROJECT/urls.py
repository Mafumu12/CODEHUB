from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/',include('MAINAPP.urls')),
    path('profile/',include('PROFILEAPP.urls')),
    path('authentication/',include('USERAUTHENTICATIONAPP.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)