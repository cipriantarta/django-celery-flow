from django.conf.urls import url
from .views import TasksView


urlpatterns = [
    url(r'^tasks/', TasksView.as_view(), name="dcf_tasks"),
]
