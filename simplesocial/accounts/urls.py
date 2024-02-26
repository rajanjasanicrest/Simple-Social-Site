from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/',views.login_user, name = 'login'),
    path('logout/',views.logout1, name = 'logout'),
    path('signup/',views.SignUp.as_view(), name = 'signup'),

]