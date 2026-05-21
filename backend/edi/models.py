from django.db import models
from erp_core.models import BaseDocument
from rest_framework import serializers, viewsets

class CodeList(BaseDocument):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Title")
    publisher = models.CharField(max_length=255, blank=True, null=True, verbose_name="Publisher")
    version = models.CharField(max_length=255, blank=True, null=True, verbose_name="Version")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    canonical_uri = models.CharField(max_length=255, blank=True, null=True, verbose_name="Canonical URI")
    publisher_id = models.CharField(max_length=255, blank=True, null=True, verbose_name="Publisher ID")
    url = models.CharField(max_length=255, blank=True, null=True, verbose_name="URL")
    default_common_code = models.ForeignKey('erp_core.CommonCode', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Default Common Code')

class CodeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeList
        fields = '__all__'

class CodeListViewSet(viewsets.ModelViewSet):
    queryset = CodeList.objects.all()
    serializer_class = CodeListSerializer

class CommonCode(BaseDocument):
    code_list = models.ForeignKey('erp_core.CodeList', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Code List')
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Title")
    applies_to = models.JSONField(default=list, blank=True, null=True, verbose_name="Applies To")
    common_code = models.CharField(max_length=255, blank=True, null=True, verbose_name="Common Code")
    additional_data = models.TextField(blank=True, null=True, verbose_name="Additional Data")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    canonical_uri = models.CharField(max_length=255, blank=True, null=True, verbose_name="Canonical URI")

class CommonCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommonCode
        fields = '__all__'

class CommonCodeViewSet(viewsets.ModelViewSet):
    queryset = CommonCode.objects.all()
    serializer_class = CommonCodeSerializer
