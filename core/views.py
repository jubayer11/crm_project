from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView


class IndexTemplateView(LoginRequiredMixin, TemplateView):

    def get_template_names(self):
        template_name = "dashboard/dashboard-4.html"
        return template_name


class dashboardjubayer(LoginRequiredMixin, TemplateView):
    def get_template_names(self):
        template_name = "dashboard-2.html"
        return template_name

