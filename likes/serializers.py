from django.contrib.auth import get_user_model
from rest_framework import serializers
from likes.models import *

class ShowExcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowExcel
        fields = ['uuid', 'video', 'audio', 'language_id', 'type', 'variant_id' ]


