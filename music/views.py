from django.shortcuts import render
from .models import Contact, Song, Album, Product
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from openpyxl import Workbook
import xlrd
import xlwt


class ExcelPageView(TemplateView):
    template_name = "excel_home.html"

from xlutils.copy import copy # http://pypi.python.org/pypi/xlutils
from xlrd import open_workbook # http://pypi.python.org/pypi/xlrd

import os
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.


def showformdata(request):
    t = Contact.objects.get(id=1)
    t.name = "Loveyou"
    t.save()


    return render(request, 'userregistration.html', dict())


def product_data(request):
    file_path = './abc.xlsx'
    wb = xlrd.open_workbook(file_path)
    wb_sheet = wb.sheet_by_index(0)
    total_rows = wb_sheet.nrows

    for rownum in range(1, total_rows):
        product_name = wb_sheet.cell(rownum, 0).value
        product_price = wb_sheet.cell(rownum, 1).value
        if product_name and product_price:
            Product.objects.filter(product_name=product_name).update(product_price=product_price)
    wb.save()
    return render(request, dict())



def export_abc_xlsx(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="abc.xlsx"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users Data') 

    row_num = 0
    columns = ['Username', 'First Name', 'Last Name', 'Email Address', ]
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num])


    rows = Product.objects.all().values_list('product_name', 'product_price')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num])
    wb.save(response)
    return render(request, dict())

























# def export_write_xls(request):
#     response = HttpResponse(content_type='application/ms-excel')
#     response['Content-Disposition'] = 'attachment; filename="users.xls"'
    
#     path = os.path.dirname(__file__)
#     template_name = "excel_home.html"
#     file = os.path.join(path, 'sample.xls')

#     rb = open_workbook(file, formatting_info=True)
#     r_sheet = rb.sheet_by_index(0)

#     wb = copy(rb)
#     ws = wb.get_sheet(0)

#     row_num = 2 # index start from 0
#     rows = User.objects.all().values_list('username', 'first_name', 'last_name', 'email')
#     for row in rows:
#         row_num += 1
#         for col_num in range(len(row)):
#             ws.write(row_num, col_num, row[col_num])
    
#     # wb.save(file) # will replace original file
#     # wb.save(file + '.out' + os.path.splitext(file)[-1]) # will save file where the excel file is
#     wb.save(response)
#     return response





# def export(request):
#     person_resource = Product()
#     dataset = person_resource.export()
#     response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
#     response['Content-Disposition'] = 'attachment; filename="persons.xls"'
#     return response

# def simple_upload(request):
#     if request.method == 'POST':
#         person_resource = PersonResource()
#         dataset = Dataset()
#         new_persons = request.FILES['myfile']

#         imported_data = dataset.load(new_persons.read(),format='xlsx')
#         #print(imported_data)
#         for data in imported_data:
#         	print(data[1])
#         	value = Person(
#         		data[0],
#         		data[1],
#         		 data[2],
#         		 data[3]
#         		)
#         	value.save()       
        
        #result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        #if not result.has_errors():
        #    person_resource.import_data(dataset, dry_run=False)  # Actually import now

    # return render(request, 'input.html')

# def export_excel(request):
#     response = HttpResponse(content_type='application/ms-excel')
#     response['Content-Disposition'] = f'attachment; filename="filename.xlsx"'

#     wb = Workbook()
#     wb.save(response)
#     return response