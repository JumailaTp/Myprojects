from . import views
from django.urls import path
app_name='credentials'
urlpatterns = [

    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('formm',views.formm,name="formm"),
    path('home',views.home,name="home"),
    path('accept',views.accept,name="accept"),




]