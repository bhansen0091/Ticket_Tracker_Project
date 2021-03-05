from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('<int:task_id>', views.render_task_id),

    path('new', views.new_task),
    path('create', views.create_task),
    path('<int:task_id>/edit', views.edit_task),
    path('<int:task_id>/delete', views.delete_task),

    path('<int:task_id>/new_subtask', views.new_subtask),
    path('<int:task_id>/create_subtask', views.create_subtask),
    path('<int:task_id>/<int:subtask_id>/edit', views.edit_subtask),
    path('<int:task_id>/<int:subtask_id>/delete', views.delete_subtask),

    path('contributors', views.view_contributors),

    path('open_tasks', views.open_tasks),
    path('<int:task_id>/add_contributor', views.add_contributor),
    

]