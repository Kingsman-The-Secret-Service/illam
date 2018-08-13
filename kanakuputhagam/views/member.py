from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from kanakuputhagam.models import Member

class MemberList(LoginRequiredMixin, ListView):
    model = Member
    template_name = 'member/list.html'
    paginate_by = 5
    ordering = ['-created_on']

class MemberCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Member
    fields = ['name']
    template_name = 'member/form.html'
    success_url = reverse_lazy('member-add')
    success_message = "%(name)s was created successfully"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class MemberUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Member
    fields = ['name']
    template_name = 'member/form.html'
    success_url = reverse_lazy('member-list')
    success_message = "%(name)s was updated successfully"

class MemberDelete(LoginRequiredMixin, DeleteView):
    model = Member
    success_url = reverse_lazy('member-list')
    success_message = "%(name)s was deleted successfully"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(MemberDelete, self).delete(request, *args, **kwargs)