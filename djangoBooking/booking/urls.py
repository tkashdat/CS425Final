from django.urls import path, include

# from views import booking
from booking import views

urlpatterns = [
    path('booking/', views.booking, name='booking'),
    path('test/', views.test)
]