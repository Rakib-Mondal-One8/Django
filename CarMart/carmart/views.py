from django.shortcuts import render, HttpResponse
from car.models import Car
from brand.models import Brand
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(ListView):
    model = Car
    template_name = 'home.html'
    context_object_name = 'cars'

    def get_queryset(self):
        queryset = super().get_queryset()
        slug = self.kwargs.get('slug')

        if slug:
            queryset = queryset.filter(brand__slug=slug)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brands"] = Brand.objects.all()
        context["selected_slug"] = self.kwargs.get('slug')
        return context
