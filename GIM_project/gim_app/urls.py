from django.urls import path
from .views import home, contact, about, service, post, post_detail

urlpatterns = [
    path('detail/<slug:slug>/', post_detail, name='detail'),
    path('', home, name='home'),
    path('about-page/', about, name='about'),
    path('contact-page/', contact, name='contact'),
    path('blog_page/', post, name='blog'),
    path('ourservice-page/', service, name='service'),
]