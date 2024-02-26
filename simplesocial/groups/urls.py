from django.urls import path
from . import views
from django.urls.converters import SlugConverter
from django.urls import register_converter

app_name = 'groups'


class SlugWithSpacesConverter(SlugConverter):
    regex = r'[-\w\s]+'
register_converter(SlugWithSpacesConverter, 'slug_with_spaces')


urlpatterns = [
    path('',views.ListGroups.as_view() , name = 'all'),
    path('new/', views.CreateGroup.as_view() , name = 'create'),
    path('posts/in/<slug_with_spaces:slug>/',views.SingleGroup.as_view(), name = 'single'),
    path('join/<slug_with_spaces:slug>/', views.JoinGroup.as_view() , name = 'join'),
    path('leave/<slug_with_spaces:slug>/', views.LeaveGroup.as_view() , name = 'leave'),
]
