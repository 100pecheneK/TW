from django.urls import path
from . import views

app_name = 'tw'
urlpatterns = [
    path('', views.all, name='all'),
    path('detail/<int:obj_id>', views.view, name='view'),
    path('done/<int:obj_id>', views.done, name='done'),
    path('in_work/<int:obj_id>', views.in_work, name='in_work'),
    path('test/<int:obj_id>', views.test, name='test'),
]
