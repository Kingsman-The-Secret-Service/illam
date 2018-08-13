from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from kanakuputhagam.models import Tag

class TagList(LoginRequiredMixin, ListView):
    model = Tag
    template_name = 'tag/list.html'
    paginate_by = 5
    ordering = ['-created_on']

class TagCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Tag
    fields = ['name']
    template_name = 'tag/form.html'
    success_url = reverse_lazy('tag-add')
    success_message = "%(name)s was created successfully"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TagUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Tag
    fields = ['name']
    template_name = 'tag/form.html'
    success_url = reverse_lazy('tag-list')
    success_message = "%(name)s was updated successfully"

class TagDelete(LoginRequiredMixin, DeleteView):
    model = Tag
    success_url = reverse_lazy('tag-list')
    success_message = "%(name)s was deleted successfully"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(TagDelete, self).delete(request, *args, **kwargs)