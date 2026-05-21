from django.db import models
from erp_core.models import BaseDocument
from rest_framework import serializers, viewsets

class VoiceCallSettings(BaseDocument):
    user = models.ForeignKey('erp_core.User', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='User')
    greeting_message = models.CharField(max_length=255, blank=True, null=True, verbose_name="Greeting Message")
    agent_busy_message = models.CharField(max_length=255, blank=True, null=True, verbose_name="Agent Busy Message")
    agent_unavailable_message = models.CharField(max_length=255, blank=True, null=True, verbose_name="Agent Unavailable Message")
    call_receiving_device = models.CharField(max_length=255, choices=[('Computer', 'Computer'), ('Phone', 'Phone')], blank=True, null=True, verbose_name='Call Receiving Device')

class VoiceCallSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoiceCallSettings
        fields = '__all__'

class VoiceCallSettingsViewSet(viewsets.ModelViewSet):
    queryset = VoiceCallSettings.objects.all()
    serializer_class = VoiceCallSettingsSerializer

class TelephonyCallType(BaseDocument):
    call_type = models.CharField(max_length=255, blank=True, null=True, verbose_name="Call Type")
    amended_from = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Amended From')

class TelephonyCallTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelephonyCallType
        fields = '__all__'

class TelephonyCallTypeViewSet(viewsets.ModelViewSet):
    queryset = TelephonyCallType.objects.all()
    serializer_class = TelephonyCallTypeSerializer

class IncomingCallSettings(BaseDocument):
    call_routing = models.CharField(max_length=255, choices=[('Sequential', 'Sequential'), ('Simultaneous', 'Simultaneous')], blank=True, null=True, verbose_name='Call Routing')
    greeting_message = models.CharField(max_length=255, blank=True, null=True, verbose_name="Greeting Message")
    agent_busy_message = models.CharField(max_length=255, blank=True, null=True, verbose_name="Agent Busy Message")
    agent_unavailable_message = models.CharField(max_length=255, blank=True, null=True, verbose_name="Agent Unavailable Message")
    call_handling_schedule = models.JSONField(default=list, blank=True, null=True, verbose_name="Call Handling Schedule")

class IncomingCallSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomingCallSettings
        fields = '__all__'

class IncomingCallSettingsViewSet(viewsets.ModelViewSet):
    queryset = IncomingCallSettings.objects.all()
    serializer_class = IncomingCallSettingsSerializer

class CallLog(BaseDocument):
    id = models.CharField(max_length=255, blank=True, null=True, verbose_name="ID")
    from = models.CharField(max_length=255, blank=True, null=True, verbose_name="From")
    to = models.CharField(max_length=255, blank=True, null=True, verbose_name="To")
    status = models.CharField(max_length=255, choices=[('Ringing', 'Ringing'), ('In Progress', 'In Progress'), ('Completed', 'Completed'), ('Failed', 'Failed'), ('Busy', 'Busy'), ('No Answer', 'No Answer'), ('Queued', 'Queued'), ('Cancelled', 'Cancelled')], blank=True, null=True, verbose_name='Status')
    duration = models.TextField(blank=True, null=True, verbose_name="Duration")
    recording_url = models.CharField(max_length=255, blank=True, null=True, verbose_name="Recording URL")
    medium = models.CharField(max_length=255, blank=True, null=True, verbose_name="Medium")
    type = models.CharField(max_length=255, choices=[('Incoming', 'Incoming'), ('Outgoing', 'Outgoing')], blank=True, null=True, verbose_name='Type')
    links = models.JSONField(default=list, blank=True, null=True, verbose_name="Links")
    summary = models.TextField(blank=True, null=True, verbose_name="Summary")
    start_time = models.DateTimeField(blank=True, null=True, verbose_name="Start Time")
    end_time = models.DateTimeField(blank=True, null=True, verbose_name="End Time")
    customer = models.ForeignKey('erp_core.Customer', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Customer')
    employee_user_id = models.ForeignKey('erp_core.User', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Employee User Id')
    type_of_call = models.ForeignKey('erp_core.TelephonyCallType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Type Of Call')
    call_received_by = models.ForeignKey('erp_core.Employee', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Call Received By')

class CallLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallLog
        fields = '__all__'

class CallLogViewSet(viewsets.ModelViewSet):
    queryset = CallLog.objects.all()
    serializer_class = CallLogSerializer

class IncomingCallHandlingSchedule(BaseDocument):
    day_of_week = models.CharField(max_length=255, choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], blank=True, null=True, verbose_name='Day Of Week')
    from_time = models.TextField(blank=True, null=True, verbose_name="From Time")
    to_time = models.TextField(blank=True, null=True, verbose_name="To Time")
    agent_group = models.ForeignKey('erp_core.EmployeeGroup', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Agent Group')

class IncomingCallHandlingScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomingCallHandlingSchedule
        fields = '__all__'

class IncomingCallHandlingScheduleViewSet(viewsets.ModelViewSet):
    queryset = IncomingCallHandlingSchedule.objects.all()
    serializer_class = IncomingCallHandlingScheduleSerializer
