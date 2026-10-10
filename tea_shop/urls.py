from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('tea-collections/', views.tea_collections, name='tea_collections'),
    path('experience/', views.experience, name='experience'),
    path('franchise/', views.franchise, name='franchise'),
    path('contact/', views.contact, name='contact'),
    path('api/teas/', views.get_teas, name='get_teas'),
    path('franchise_enquiry/', views.franchise_enquiry, name='franchise_enquiry'),
]
