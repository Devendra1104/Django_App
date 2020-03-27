from django.urls import path
from app_two import views

urlpatterns = [
    path('',views.indexx,name='indexx'),
    path('users/',views.index,name='index'),
]