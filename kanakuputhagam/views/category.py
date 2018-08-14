from django.urls import reverse_lazy
from django.contrib import messages
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from kanakuputhagam.models import Category

class CategoryList(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'category/list.html'
    paginate_by = 5

    def get_queryset(self):
        return super().get_queryset().filter(
                user = self.request.user)

class CategoryCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Category
    fields = ['type', 'name', 'color']
    template_name = 'category/form.html'
    success_url = reverse_lazy('category-add')
    success_message = "%(type)s - %(name)s was created successfully"

    def form_valid(self, form):
        if Category.objects.filter(user = self.request.user, type = form.cleaned_data['type'], name = form.cleaned_data['name']).exists():
            form.add_error('name', 'The combination of "' + form.cleaned_data['type'] + '" type & "' + form.cleaned_data['name'] + '" name already exists')
            return super().form_invalid(form)
        form.instance.user = self.request.user
        return super().form_valid(form)

class CategoryUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Category
    fields = ['type', 'name', 'color']
    template_name = 'category/form.html'
    success_url = reverse_lazy('category-list')
    success_message = "%(type)s - %(name)s was updated successfully"

    def get_queryset(self):
        return super().get_queryset().filter(
                user=self.request.user)

    def form_valid(self, form):
        if Category.objects.filter(user = self.request.user, type = form.cleaned_data['type'], name = form.cleaned_data['name']).exists():
            form.add_error('name', 'The combination of "' + form.cleaned_data['type'] + '" type & "' + form.cleaned_data['name'] + '" name already exists')
            return super().form_invalid(form)
        form.instance.user = self.request.user
        return super().form_valid(form)

class CategoryDelete(LoginRequiredMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('category-list')
    success_message = "%(type)s - %(name)s was deleted successfully"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user == request.user:
            messages.success(self.request, self.success_message % obj.__dict__)
            return super().delete(request, *args, **kwargs)
        else:
            raise Http404