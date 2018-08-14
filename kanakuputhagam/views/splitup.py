from django.urls import reverse_lazy
from django.contrib import messages
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from kanakuputhagam.models import Splitup, Category

class SplitupList(LoginRequiredMixin, ListView):
    model = Splitup
    template_name = 'splitup/list.html'
    paginate_by = 5

    def get_queryset(self):
        return super().get_queryset().filter(
                user = self.request.user)

class SplitupCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Splitup
    fields = ['budget', 'category', 'member', 'tag', 'amount', 'description']
    template_name = 'splitup/form.html'
    success_url = reverse_lazy('splitup-add')
    success_message = "Sliptup %(category)s was created successfully"

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.type = Category.objects.filter(id=form.data['category']).first().type
        return super().form_valid(form)

class SplitupUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Splitup
    fields = ['budget', 'category', 'member', 'tag', 'amount', 'description']
    template_name = 'splitup/form.html'
    success_url = reverse_lazy('splitup-list')
    success_message = "Sliptup with category %(category)s was updated successfully"

    def get_queryset(self):
        return super().get_queryset().filter(
                user=self.request.user)

    def form_valid(self, form):
        form.instance.type = Category.objects.filter(id=form.data['category']).first().type
        return super().form_valid(form)

class SplitupDelete(LoginRequiredMixin, DeleteView):
    model = Splitup
    success_url = reverse_lazy('splitup-list')
    success_message = "%(type)s was deleted successfully"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user == request.user:
            messages.success(self.request, self.success_message % obj.__dict__)
            return super().delete(request, *args, **kwargs)
        else:
            raise Http404