from django.conf import settings
from django.urls import path,include
from django.conf.urls.static import static
from . import views
app_name = 'login'
urlpatterns = [
    path('', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    path('confirm/', views.user_confirm)
]