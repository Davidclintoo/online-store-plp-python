from django.urls import path
from. import views

urlpatterns = [
    path('login/', views.login, name= 'Customer-login'),
    path('register/', views.register, name= 'Customer-signup'),

]