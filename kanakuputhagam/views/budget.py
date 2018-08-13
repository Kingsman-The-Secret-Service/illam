from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from kanakuputhagam.models import Budget

class BudgetList(LoginRequiredMixin, ListView):
    model = Budget
    template_name = 'budget/list.html'
    paginate_by = 5
    ordering = ['-start_date']

class BudgetCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Budget
    fields = ['name', 'start_date', 'end_date', 'description']
    template_name = 'budget/form.html'
    success_url = reverse_lazy('budget-add')
    success_message = "%(name)s was created successfully"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BudgetUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Budget
    fields = ['name', 'start_date', 'end_date', 'description']
    template_name = 'budget/form.html'
    success_url = reverse_lazy('budget-list')
    success_message = "%(name)s was updated successfully"

class BudgetDelete(LoginRequiredMixin, DeleteView):
    model = Budget
    success_url = reverse_lazy('budget-list')
    success_message = "%(name)s was deleted successfully"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(BudgetDelete, self).delete(request, *args, **kwargs)