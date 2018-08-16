from django.urls import reverse_lazy
from django.contrib import messages
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from kanakuputhagam.models import Splitup, Budget, Category, Member, Tag

class SplitupList(LoginRequiredMixin, ListView):
    model = Splitup
    template_name = 'splitup/list.html'
    paginate_by = 5

    def get_queryset(self):
        return super().get_queryset().filter(
                user = self.request.user)

class SplitupCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Splitup
    fields = ['budget', 'category', 'member', 'amount', 'tag', 'description']
    template_name = 'splitup/form.html'
    success_url = reverse_lazy('splitup-list')
    success_message = "Sliptup %(category)s was created successfully"

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)

        if 'type' in self.kwargs.keys() and self.kwargs['type'] in ['INCOME', 'SAVING', 'EXPENSE']:
            form.fields['category'].queryset = Category.objects.filter(
                user=self.request.user, 
                type=self.kwargs['type'])
        else:
            form.fields['category'].queryset = Category.objects.filter(user=self.request.user)

        form.fields['budget'].queryset = Budget.objects.filter(user=self.request.user)
        form.fields['member'].queryset = Member.objects.filter(user=self.request.user)
        form.fields['tag'].queryset = Tag.objects.filter(user=self.request.user)
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.type = Category.objects.filter(id=form.data['category']).first().type
        return super().form_valid(form)

class SplitupUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Splitup
    fields = ['budget', 'category', 'member', 'amount', 'tag', 'description']
    template_name = 'splitup/form.html'
    success_url = reverse_lazy('splitup-list')
    success_message = "Sliptup with category %(category)s was updated successfully"

    def get_queryset(self):
        return super().get_queryset().filter(
                user=self.request.user)

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.fields['budget'].queryset = Budget.objects.filter(user=self.request.user)
        form.fields['category'].queryset = Category.objects.filter(user=self.request.user)
        form.fields['member'].queryset = Member.objects.filter(user=self.request.user)
        form.fields['tag'].queryset = Tag.objects.filter(user=self.request.user)
        return form

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