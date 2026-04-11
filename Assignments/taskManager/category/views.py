from django.shortcuts import render, redirect

from category.forms import CategoryForm


# Create your views here.
def add(request):
	if request.method == "POST":
		form = CategoryForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	form = CategoryForm()
	return render(request,'category_add.html',{'form':form})