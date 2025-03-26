from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from .models import Recipe, RecipeIngredient, RecipeImage
from .forms import RecipeForm, RecipeImageForm


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = 'ledger/recipe_add.html'
    form_class = RecipeForm
    success_url = reverse_lazy('ledger:recipe_list')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            r = Recipe()
            r.author = self.request.user
            r.save()
            return redirect(self.success_url)
        else:
            return self.form_invalid(form)


class RecipeImageCreateView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    template_name = 'ledger/recipe_add_image.html'
    form_class = RecipeImageForm

    def get_success_url(self):
        return reverse_lazy('ledger:recipe-detail', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['recipe'] = Recipe.objects.get(pk=self.kwargs['pk'])
        ctx['form'] = RecipeImageForm()
        return ctx

    def post(self, request, *args, **kwargs):
        recipe = Recipe.objects.get(pk=kwargs['pk'])
        form = RecipeImageForm(request.POST, request.FILES)
        
        if form.is_valid():
            i = form.save(commit=False)
            i.recipe = recipe
            i.save()
            self.object = i
            return redirect(self.get_success_url())
        else:
            self.object_list = self.get_queryset(**kwargs)
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)


class RecipeListView(ListView):
    model = Recipe
    template_name = 'ledger/recipe_list.html'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'ledger/recipe_detail.html'
    redirect_field_name = 'registration/login.html'
