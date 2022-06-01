from .models import Event
from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect)
from .models import GeeksModel
import xlsxwriter
from django.http import HttpResponse
from openpyxl.styles import Font
# Create your views here.




def geeks_show(request):
    t = GeeksModel.objects.get(id=1)
    t.title = "Why so serious"
    t.biography = "Joker"
    t.save()
    return render(request, 'geeks_event.html', dict())



def export_data(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=mymodel.xlsx'
    workbook = xlsxwriter.Workbook('hello.xlsx')
    worksheet = workbook.add_worksheet()

    scores = Event.objects.all().values_list(
    ['id', 1000],
    ['event_date', 100],
    ['venue',  300],
    ['manager', 50],
    ['description', 76]
    )
    row = 0
    col = 0

    # export data to Excel

    for name, score in (scores):
        worksheet.write(row, col, name)
        worksheet.write(row, col + 1, score)
        row += 1
   
    workbook.close()
    return render(request, dict())














































# # after updating it will redirect to detail_View
# def detail_view(request, id):
# 	# dictionary for initial data with
# 	# field names as keys
# 	context ={}

# 	# add the dictionary during initialization
# 	context["data"] = GeeksModel.objects.get(id = id)
		
# 	return render(request, "detail_view.html", context)

# # update view for details
# def update_view(request, id):
# 	# dictionary for initial data with
# 	# field names as keys
# 	context ={}

# 	# fetch the object related to passed id
# 	obj = get_object_or_404(GeeksModel, id = id)

# 	# pass the object as instance in form
# 	form = GeeksForm(request.POST or None, instance = obj)

# 	# save the data from the form and
# 	# redirect to detail_view
# 	if form.is_valid():
# 		form.save()
# 		return HttpResponseRedirect("/"+id)

# 	# add form dictionary to context
# 	context["form"] = form

# 	return render(request, "update_view.html", context)

