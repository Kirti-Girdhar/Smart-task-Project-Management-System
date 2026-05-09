from django.urls import path
# from tasks.views import task_list,task_detail
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet


# urlpatterns=[
#     path('tasks/', task_list),
#     path('tasks/<int:id>/', task_detail),
# ]

router= DefaultRouter()
router.register('tasks', TaskViewSet)
urlpatterns= router.urls
