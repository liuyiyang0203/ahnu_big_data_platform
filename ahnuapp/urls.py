from django.urls import path, include
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('teachers/', views.teachers, name='teachers'),
    path('achievements/', views.achievements, name='achievements'),
    path('user_logout/', views.user_logout, name='user_logout'),
]