from django.contrib import admin
from django.urls import path
from .views import HomeView
from accounts.views import new_user,login_user
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView, name='home'),
    path('register', new_user, name='register_new_user'),
    path('login', login_user, name='login_user'),
]