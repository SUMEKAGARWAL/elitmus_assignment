from django.urls import path
from .import views
urlpatterns = [
    path('', views.index, name = 'index'),
    path('registration/', views.registration, name = 'registration'),
    path('login/', views.user_login, name = 'login'),
    path('logout/', views.user_logout, name = 'logout'),
    path('create/', views.create, name = 'create'),
    path('home/', views.home, name = 'home'),
    path("delete_contact/<str:pk>/", views.delete_contact, name="delete_contact"),
]