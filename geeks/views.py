from django.shortcuts import render
from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect)
from .models import GeeksModel
from .forms import GeeksForm
# Create your views here.

# after updating it will redirect to detail_View
def detail_view(request, id):
	# dictionary for initial data with
	# field names as keys
	context ={}

	# add the dictionary during initialization
	context["data"] = GeeksModel.objects.get(id = id)
		
	return render(request, "detail_view.html", context)

# update view for details
def update_view(request, id):
	# dictionary for initial data with
	# field names as keys
	context ={}

	# fetch the object related to passed id
	obj = get_object_or_404(GeeksModel, id = id)

	# pass the object as instance in form
	form = GeeksForm(request.POST or None, instance = obj)

	# save the data from the form and
	# redirect to detail_view
	if form.is_valid():
		form.save()
		return HttpResponseRedirect("/"+id)

	# add form dictionary to context
	context["form"] = form

	return render(request, "update_view.html", context)

