from django.urls import path
from . import views
app_name = 'user_example'
urlpatterns = [
    path('', views.index, name='index'),
]
