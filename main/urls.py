from django.urls import path
from main import views
app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('join_session/', views.join_session, name='join_session'),
    path('about_us/', views.about_us, name='about_us'),
]

