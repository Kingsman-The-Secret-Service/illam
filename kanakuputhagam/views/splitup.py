from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from kanakuputhagam.models import Splitup

class SplitupList(LoginRequiredMixin, ListView):
    model = Splitup
    template_name = 'splitup/list.html'
    paginate_by = 5
    ordering = ['-created_on']

class SplitupCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Splitup
    fields = ['type', 'budget', 'category', 'member', 'tag', 'amount', 'description']
    template_name = 'splitup/form.html'
    success_url = reverse_lazy('splitup-add')
    success_message = "%(type)s - %(category)s was created successfully"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class SplitupUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Splitup
    fields = ['type', 'budget', 'category', 'member', 'tag', 'amount', 'description']
    template_name = 'splitup/form.html'
    success_url = reverse_lazy('splitup-list')
    success_message = "%(type)s - %(category)s was updated successfully"

class SplitupDelete(LoginRequiredMixin, DeleteView):
    model = Splitup
    success_url = reverse_lazy('splitup-list')
    success_message = "%(type)s was deleted successfully"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(SplitupDelete, self).delete(request, *args, **kwargs)