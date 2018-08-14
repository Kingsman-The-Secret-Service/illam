from django.urls import reverse_lazy
from django.contrib import messages
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from kanakuputhagam.models import Tag

class TagList(LoginRequiredMixin, ListView):
    model = Tag
    template_name = 'tag/list.html'
    paginate_by = 5

    def get_queryset(self):
        return super().get_queryset().filter(
                user = self.request.user)

class TagCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Tag
    fields = ['name']
    template_name = 'tag/form.html'
    success_url = reverse_lazy('tag-add')
    success_message = "%(name)s was created successfully"

    def form_valid(self, form):
        if Tag.objects.filter(user = self.request.user, name = form.cleaned_data['name']).exists():
            form.add_error('name', '"' + form.cleaned_data['name'] + '" name already exists')
            return super().form_invalid(form)
        form.instance.user = self.request.user
        return super().form_valid(form)

class TagUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Tag
    fields = ['name']
    template_name = 'tag/form.html'
    success_url = reverse_lazy('tag-list')
    success_message = "%(name)s was updated successfully"

    def get_queryset(self):
        return super().get_queryset().filter(
                user=self.request.user)
    
    def form_valid(self, form):
        if Tag.objects.filter(user = self.request.user, name = form.cleaned_data['name']).exists():
            form.add_error('name', '"' + form.cleaned_data['name'] + '" name already exists')
            return super().form_invalid(form)
        return super().form_valid(form)

class TagDelete(LoginRequiredMixin, DeleteView):
    model = Tag
    success_url = reverse_lazy('tag-list')
    success_message = "%(name)s was deleted successfully"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user == request.user:
            messages.success(self.request, self.success_message % obj.__dict__)
            return super().delete(request, *args, **kwargs)
        else:
            raise Http404