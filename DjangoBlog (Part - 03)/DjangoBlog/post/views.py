from django.shortcuts import render,redirect
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from django.urls import reverse_lazy

# Create your views here.

# @login_required
# def add_post(request):
#     if(request.method == 'POST'):
#         form = forms.PostForm(request.POST)
#         if(form.is_valid()):
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#             form.save_m2m()
#             return redirect("add_post")
#     else:
#         form = forms.PostForm()
#     return render(request, 'post_add.html',{'form':form})


# @login_required
@method_decorator(login_required,name='dispatch')
class AddPostCreateView(CreateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('add_post')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# @login_required
# def edit_post(request,id):
#     post = models.Post.objects.get(pk=id)

#     if(request.method == 'POST'):
#         form = forms.PostForm(request.POST,instance=post)
#         if(form.is_valid()):
#             # form.instance.author = request.user
#             form.save()
#             return redirect('profile')
#     else:
#         form = forms.PostForm(instance=post)
#     return render(request,'post_edit.html',{'form':form})


@method_decorator(login_required, name="dispatch")
class UpdatePostView(UpdateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'

# @login_required
# def delete_post(request,id):
#     post = models.Post.objects.get(pk=id)
#     post.delete()
#     return redirect('profile')


@method_decorator(login_required, name="dispatch")
class DeletePostView(DeleteView):
    model = models.Post
    pk_url_kwarg = 'id'
    template_name = 'delete.html'
    success_url = reverse_lazy('profile')


class DetailsPostView(DetailView):
    model = models.Post
    template_name = 'details.html'
    pk_url_kwarg = 'id'
    form_class = forms.CommentForm

    def post(self,request,*args,**kwargs):
        self.object = self.get_object()
        form = self.form_class(request.POST)

        if(form.is_valid()):
            comment = form.save(commit=False)
            comment.post = self.object
            comment.save()

        return redirect('details_post',id=self.object.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context
