from django.urls import path
from tasks.views import task_list,task_detail

urlpatterns=[
    path('tasks/', task_list),
    path('tasks/<int:id>/', task_detail),
]
