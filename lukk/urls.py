from django.urls import path
import lukk.views

urlpatterns = [
    path('',lukk.views.home,name='home'),
    path('home', lukk.views.home, name='home'),
    path('login', lukk.views.login, name='login'),
    path('logout', lukk.views.logout, name='logout'),
    path('admin_home', lukk.views.admin_home, name='admin_home'),
    path('download_csv', lukk.views.download_csv, name='download_csv'),
]