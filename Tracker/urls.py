from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include("login.urls")),
    path('holidays/', include("holidays.urls")),
    path('insurance/', include("insurance.urls")),
    path('timer/', include("timer.urls")),
    path('leave/', include("leave.urls")),
    path('', include("home.urls")),
    path('contact/', include("contact.urls")),
]

#urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
