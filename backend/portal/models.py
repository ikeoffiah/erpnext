from django.db import models
from erp_core.models import BaseDocument
from rest_framework import serializers, viewsets

class WebsiteFilterField(BaseDocument):
    fieldname = models.TextField(blank=True, null=True, verbose_name="Fieldname")

class WebsiteFilterFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebsiteFilterField
        fields = '__all__'

class WebsiteFilterFieldViewSet(viewsets.ModelViewSet):
    queryset = WebsiteFilterField.objects.all()
    serializer_class = WebsiteFilterFieldSerializer

class WebsiteAttribute(BaseDocument):
    attribute = models.ForeignKey('erp_core.ItemAttribute', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Attribute')

class WebsiteAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebsiteAttribute
        fields = '__all__'

class WebsiteAttributeViewSet(viewsets.ModelViewSet):
    queryset = WebsiteAttribute.objects.all()
    serializer_class = WebsiteAttributeSerializer
