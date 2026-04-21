from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from . import models
from .forms import CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def order(request,pk):
    car = models.Car.objects.get(pk=pk)
    models.Order.objects.create(
        user = request.user,
        car = car
    )
    car.quantity-=1
    car.save()

    return redirect('profile')

class CarDetailView(DetailView):
    model = models.Car
    template_name = 'details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        context["comments"] = self.object.comments.all().order_by('-created_at')
        return context

    def post(self,request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)

        if form.is_valid() and request.user.is_authenticated:
            comment = form.save(commit=False)
            comment.user = request.user
            comment.car = self.object
            comment.save()

        return redirect('car_details',pk=self.object.pk)
