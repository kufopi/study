from  django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('room/<int:pk>/', views.room, name='room'),
    path('create-room/',views.createRoom, name='create_room'),
    path('update-room/<int:pk>',views.updateRoom, name='update'),
    path('delete-room/<int:pk>', views.deleteRoom, name='delete_room'),
    path('door/',views.loginPage, name='login'),
    path('connect/',views.joinuser, name='join'),
    path('exit/', views.logoutPage, name='logout'),
    path('com-del/<int:pk>',views.deleteComment, name='delete_message'),
    path('profile/<int:pk>', views.userProfile, name='profile'),
    path('user-update/', views.updateUser, name='user-update'),
    path('topics/',views.topicsPage, name='topics'),
    path('activity/',views.activist, name='activity'),
]
