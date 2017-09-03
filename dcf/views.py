from django.views.generic import TemplateView


class TasksView(TemplateView):
    template_name = "admin/dcf/tasks.html"

    def get(self, request):
        return super().get(request)
