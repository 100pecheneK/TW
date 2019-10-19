from django.urls import path
from . import views

app_name = 'ob'
urlpatterns = [
    path('/', views.view, name='view'),
]
