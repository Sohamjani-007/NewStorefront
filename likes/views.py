import xlrd
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from collections import OrderedDict
import json
from rest_framework.views import APIView
from likes.models import ShowExcel
from likes.serializers import ShowExcelSerializer

# Create your views here.


class GetShowExcelApiView(APIView):
    def get(self, request, format=None):

        excel = ShowExcel.objects.all()
        print(excel.count())

        return Response("Got Data")


class ShowExcelApiView(APIView):
    """
    List all expenses and newly created.
    """

    def post(self, request, format=None):
        print(request.data)
        file = request.data.get('file')
        print(file)
        wb = xlrd.open_workbook(file_contents=file.read(),
                                on_demand=True, ragged_rows=True)
        ws = wb.sheet_by_index(0)
        data_list = []
        for rownum in range(1, ws.nrows):
            data = dict()
            row_values = ws.row_values(rownum)
            data['uuid'] = row_values[3]
            data['video'] = row_values[4]
            data['audio'] = row_values[5]
            st = data['is_active'] = row_values[6]
            if st == 'true':
                st = True
            else:
                st = False
            data['is_active'] = row_values[6] = st
            data['language_id'] = row_values[7]
            data['type'] = row_values[8]
            data['variant_id'] = row_values[9]
            print(data)
            data_list.append(data)
            ShowExcel.objects.create(**data)


        return Response(data_list, status=status.HTTP_201_CREATED)
