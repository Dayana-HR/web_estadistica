from web_estadistica import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/',views.home)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
