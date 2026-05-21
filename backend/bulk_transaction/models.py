from django.db import models
from erp_core.models import BaseDocument
from rest_framework import serializers, viewsets

class BulkTransactionLog(BaseDocument):
    date = models.DateField(blank=True, null=True, verbose_name="Date")
    log_entries = models.IntegerField(default=0, verbose_name="Log Entries")
    succeeded = models.IntegerField(default=0, verbose_name="Succeeded")
    failed = models.IntegerField(default=0, verbose_name="Failed")

class BulkTransactionLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BulkTransactionLog
        fields = '__all__'

class BulkTransactionLogViewSet(viewsets.ModelViewSet):
    queryset = BulkTransactionLog.objects.all()
    serializer_class = BulkTransactionLogSerializer

class BulkTransactionLogDetail(BaseDocument):
    transaction_name = models.TextField(blank=True, null=True, verbose_name="Name")
    transaction_status = models.CharField(max_length=255, blank=True, null=True, verbose_name="Status")
    error_description = models.TextField(blank=True, null=True, verbose_name="Error Description")
    from_doctype = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='From Doctype')
    to_doctype = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='To Doctype')
    date = models.DateField(blank=True, null=True, verbose_name="Date ")
    time = models.TextField(blank=True, null=True, verbose_name="Time")
    retried = models.IntegerField(default=0, verbose_name="Retried")

class BulkTransactionLogDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BulkTransactionLogDetail
        fields = '__all__'

class BulkTransactionLogDetailViewSet(viewsets.ModelViewSet):
    queryset = BulkTransactionLogDetail.objects.all()
    serializer_class = BulkTransactionLogDetailSerializer
