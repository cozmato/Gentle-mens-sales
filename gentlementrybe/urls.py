from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler400, handler500, handler404, handler403
from django.views.generic import TemplateView
from collection import views as app_view
from django.views.static import serve
# from joe.views import ServiceWorker

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('collection.urls')),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root':settings.STATIC_ROOT})
]

handler404 = app_view.error_404

handler500 = app_view.error_500

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
