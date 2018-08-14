from django.urls import reverse_lazy
from django.contrib import messages
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from kanakuputhagam.models import Budget

class BudgetList(LoginRequiredMixin, ListView):
    model = Budget
    template_name = 'budget/list.html'
    paginate_by = 5
    
    def get_queryset(self):
        return super().get_queryset().filter(
                user = self.request.user)

class BudgetCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Budget
    fields = ['name', 'start_date', 'end_date', 'description']
    template_name = 'budget/form.html'
    success_url = reverse_lazy('budget-add')
    success_message = "%(name)s was created successfully"

    def form_valid(self, form):
        if Budget.objects.filter(user = self.request.user, start_date = form.cleaned_data['start_date'], end_date = form.cleaned_data['end_date']).exists():
            form.add_error('end_date', 'The combination of "' + form.cleaned_data['start_date'].strftime("%d-%m-%Y") + '" start & "' + form.cleaned_data['end_date'].strftime("%d-%m-%Y") + '" end date already exists')
            return super().form_invalid(form)
        form.instance.user = self.request.user
        return super().form_valid(form)

class BudgetUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Budget
    fields = ['name', 'start_date', 'end_date', 'description']
    template_name = 'budget/form.html'
    success_url = reverse_lazy('budget-list')
    success_message = "%(name)s was updated successfully"

    def get_queryset(self):
        return super().get_queryset().filter(
                user=self.request.user)

    def form_valid(self, form):
        if Budget.objects.filter(user = self.request.user, start_date = form.cleaned_data['start_date'], end_date = form.cleaned_data['end_date']).exists():
            form.add_error('end_date', 'The combination of "' + form.cleaned_data['start_date'].strftime("%d-%m-%Y") + '" start & "' + form.cleaned_data['end_date'].strftime("%d-%m-%Y") + '" end date already exists')
            return super().form_invalid(form)
        form.instance.user = self.request.user
        return super().form_valid(form)

class BudgetDelete(LoginRequiredMixin, DeleteView):
    model = Budget
    success_url = reverse_lazy('budget-list')
    success_message = "%(name)s was deleted successfully"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user == request.user:
            messages.success(self.request, self.success_message % obj.__dict__)
            return super().delete(request, *args, **kwargs)
        else:
            raise Http404