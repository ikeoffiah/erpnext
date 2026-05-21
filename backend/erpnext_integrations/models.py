from django.db import models
from erp_core.models import BaseDocument
from rest_framework import serializers, viewsets

class PlaidSettings(BaseDocument):
    enabled = models.BooleanField(default=False, verbose_name="Enabled")
    automatic_sync = models.BooleanField(default=False, verbose_name="Synchronize all accounts every hour")
    plaid_client_id = models.CharField(max_length=255, blank=True, null=True, verbose_name="Plaid Client ID")
    plaid_secret = models.TextField(blank=True, null=True, verbose_name="Plaid Secret")
    plaid_env = models.CharField(max_length=255, choices=[('sandbox', 'sandbox'), ('development', 'development'), ('production', 'production')], blank=True, null=True, verbose_name='Plaid Environment')
    enable_european_access = models.BooleanField(default=False, verbose_name="Enable European Access")

class PlaidSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaidSettings
        fields = '__all__'

class PlaidSettingsViewSet(viewsets.ModelViewSet):
    queryset = PlaidSettings.objects.all()
    serializer_class = PlaidSettingsSerializer
