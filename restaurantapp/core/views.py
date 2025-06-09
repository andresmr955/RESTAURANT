from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.

class HomeView(TemplateView):
    template_name = 'base.html'

    
    
class DashboardAdminView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = "admin_dashboard.html"

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_manager()