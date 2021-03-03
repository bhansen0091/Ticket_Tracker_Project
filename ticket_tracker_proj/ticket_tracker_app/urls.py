from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard),

    path('new', views.new_task),
    path('create', views.create_task),
    path('<int:task_id>/edit', views.edit_task),
    path('<int:task_id>/update', views.update_task),

    path('new_subtask', views.new_subtask),
    path('create_subtask', views.create_subtask),
    path('<int:task_id>/<int:subtask_id>/edit', views.edit_subtask),
    path('<int:task_id>/<int:subtask_id>/update', views.update_subtask),
    

]