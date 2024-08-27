from django.urls import path
#from .utils import HashIdConverter
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name="about"),
    path('privacy', views.privacy, name="privacy"),
    path('contact', views.contact, name="contact"),
    path('product/<category>/<id>', views.product, name="product"),
    path('post/<name>/<pk>/', views.post_detail, name='post-detail'),
    # path('search', views.search, name='search'),
    # path('searchfilter', views.searchfilter, name='search-filter'),
    # path('ajaxsearch', views.ajaxsearch, name='ajaxsearch'),
]
