from django.contrib import admin
from django.conf.urls import url, include
from . import urls
from django.template.response import TemplateResponse


class DCFAdmin(admin.AdminSite):
    def get_urls(self):
        base_urls = super(DCFAdmin, self).get_urls()
        dcf_urls = [
            url(r'^$', self.tasks_view, name="dcf_tasks"),
        ]
        return dcf_urls + base_urls

    def tasks_view(self, request):
        context = dict(
            self.each_context(request),
        )
        return TemplateResponse(request, "admin/dcf/tasks.html", context)

site = DCFAdmin(name="dcfadmin")
