from django.urls import path
from django.contrib import admin
from . import views
from .views import home,createRoom,updateRoom,deleteRoom,room
urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('', views.home, name="home"),
    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
    path('delete-message/<str:pk>/', views.deleteMessage, name="delete-message"),
    path('update-user/', views.updateUser, name="update-user"),
    path('topics/', views.topicsPage, name="topics"),
    path('activity/', views.activityPage, name="activity"),
    path('room/<str:pk>/', views.room, name="room"),
]
