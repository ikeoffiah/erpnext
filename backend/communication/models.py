from django.db import models
from erp_core.models import BaseDocument
from rest_framework import serializers, viewsets

class CommunicationMedium(BaseDocument):
    communication_medium_type = models.CharField(max_length=255, choices=[('Voice', 'Voice'), ('Email', 'Email'), ('Chat', 'Chat')], blank=True, null=True, verbose_name='Communication Medium Type')
    catch_all = models.ForeignKey('erp_core.EmployeeGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Catch All')
    provider = models.ForeignKey('erp_core.Supplier', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Provider')
    disabled = models.BooleanField(default=False, verbose_name="Disabled")
    timeslots = models.JSONField(default=list, blank=True, null=True, verbose_name="Timeslots")
    communication_channel = models.CharField(max_length=255, choices=[], blank=True, null=True, verbose_name='Communication Channel')

class CommunicationMediumSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunicationMedium
        fields = '__all__'

class CommunicationMediumViewSet(viewsets.ModelViewSet):
    queryset = CommunicationMedium.objects.all()
    serializer_class = CommunicationMediumSerializer

class CommunicationMediumTimeslot(BaseDocument):
    day_of_week = models.CharField(max_length=255, choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], blank=True, null=True, verbose_name='Day of Week')
    from_time = models.TextField(blank=True, null=True, verbose_name="From Time")
    to_time = models.TextField(blank=True, null=True, verbose_name="To Time")
    employee_group = models.ForeignKey('erp_core.EmployeeGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Employee Group')

class CommunicationMediumTimeslotSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunicationMediumTimeslot
        fields = '__all__'

class CommunicationMediumTimeslotViewSet(viewsets.ModelViewSet):
    queryset = CommunicationMediumTimeslot.objects.all()
    serializer_class = CommunicationMediumTimeslotSerializer
