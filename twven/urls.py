from django.urls import path
from . import views

app_name = 'tw'
urlpatterns = [
    # Вид
    path('/all', views.view_all, name='all'),
    path('/detail/<int:obj_id>', views.detail_view, name='view'),
    # Действия
    path('/done/<int:obj_id>', views.done, name='done'),
    path('/in_work/<int:obj_id>', views.in_work, name='in_work'),
    # Для бота
    path('/reload', views.reload, name='reload'),
]
