import xlrd
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from collections import OrderedDict
import json
from rest_framework.views import APIView

# Create your views here.


class ShowExcelApiView(APIView):
    """
    List all expenses and newly created.
    """

    def post(self, request, format=None):
        print(request.data)
        file = request.data.get('file')
        wb = xlrd.open_workbook(file_contents=file.read(), on_demand=True, ragged_rows=True)
        ws = wb.sheet_by_index(0)
        data_list = []
        for rownum in range(1, ws.nrows):
            data = dict()
            row_values = ws.row_values(rownum)
            data['id'] = row_values[0]
            data['created'] = row_values[1]
            data['modified'] = row_values[2]
            data['uuid'] = row_values[3]
            data['video'] = row_values[4]
            data['audio'] = row_values[5]
            data['is_active'] = row_values[6]
            data['language_id'] = row_values[7]
            data['type'] = row_values[8]
            data['variant_id'] = row_values[9]
            data_list.append(data)                     
        return Response(data_list, status=status.HTTP_201_CREATED)

 