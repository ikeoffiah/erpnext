from django.db import models
from erp_core.models import BaseDocument
from rest_framework import serializers, viewsets

class QualityGoal(BaseDocument):
    frequency = models.CharField(max_length=255, choices=[('None', 'None'), ('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly'), ('Quarterly', 'Quarterly')], blank=True, null=True, verbose_name='Monitoring Frequency')
    procedure = models.ForeignKey('erp_core.QualityProcedure', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Procedure')
    date = models.CharField(max_length=255, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30')], blank=True, null=True, verbose_name='Date')
    weekday = models.CharField(max_length=255, choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday')], blank=True, null=True, verbose_name='Weekday')
    objectives = models.JSONField(default=list, blank=True, null=True, verbose_name="Objectives")
    goal = models.CharField(max_length=255, blank=True, null=True, verbose_name="Goal")

class QualityGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualityGoal
        fields = '__all__'

class QualityGoalViewSet(viewsets.ModelViewSet):
    queryset = QualityGoal.objects.all()
    serializer_class = QualityGoalSerializer

class NonConformance(BaseDocument):
    subject = models.CharField(max_length=255, blank=True, null=True, verbose_name="Subject")
    procedure = models.ForeignKey('erp_core.QualityProcedure', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Procedure')
    status = models.CharField(max_length=255, choices=[('Open', 'Open'), ('Resolved', 'Resolved'), ('Cancelled', 'Cancelled')], blank=True, null=True, verbose_name='Status')
    details = models.TextField(blank=True, null=True, verbose_name="Details")
    process_owner = models.CharField(max_length=255, blank=True, null=True, verbose_name="Process Owner")
    full_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Full Name")
    corrective_action = models.TextField(blank=True, null=True, verbose_name="Corrective Action")
    preventive_action = models.TextField(blank=True, null=True, verbose_name="Preventive Action")

class NonConformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = NonConformance
        fields = '__all__'

class NonConformanceViewSet(viewsets.ModelViewSet):
    queryset = NonConformance.objects.all()
    serializer_class = NonConformanceSerializer

class QualityFeedbackParameter(BaseDocument):
    parameter = models.CharField(max_length=255, blank=True, null=True, verbose_name="Parameter")
    rating = models.CharField(max_length=255, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], blank=True, null=True, verbose_name='Rating')
    feedback = models.TextField(blank=True, null=True, verbose_name="Feedback")

class QualityFeedbackParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualityFeedbackParameter
        fields = '__all__'

class QualityFeedbackParameterViewSet(viewsets.ModelViewSet):
    queryset = QualityFeedbackParameter.objects.all()
    serializer_class = QualityFeedbackParameterSerializer

class QualityProcedureProcess(BaseDocument):
    process_description = models.TextField(blank=True, null=True, verbose_name="Process Description")
    procedure = models.ForeignKey('erp_core.QualityProcedure', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Sub Procedure')

class QualityProcedureProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualityProcedureProcess
        fields = '__all__'

class QualityProcedureProcessViewSet(viewsets.ModelViewSet):
    queryset = QualityProcedureProcess.objects.all()
    serializer_class = QualityProcedureProcessSerializer

class QualityAction(BaseDocument):
    goal = models.ForeignKey('erp_core.QualityGoal', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Goal')
    date = models.DateField(blank=True, null=True, verbose_name="Date")
    procedure = models.ForeignKey('erp_core.QualityProcedure', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Procedure')
    status = models.CharField(max_length=255, choices=[('Open', 'Open'), ('Completed', 'Completed')], blank=True, null=True, verbose_name='Status')
    corrective_preventive = models.CharField(max_length=255, choices=[('Corrective', 'Corrective'), ('Preventive', 'Preventive')], blank=True, null=True, verbose_name='Corrective/Preventive')
    resolutions = models.JSONField(default=list, blank=True, null=True, verbose_name="Resolutions")
    review = models.ForeignKey('erp_core.QualityReview', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Review')
    feedback = models.ForeignKey('erp_core.QualityFeedback', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Feedback')

class QualityActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualityAction
        fields = '__all__'

class QualityActionViewSet(viewsets.ModelViewSet):
    queryset = QualityAction.objects.all()
    serializer_class = QualityActionSerializer

class QualityFeedbackTemplate(BaseDocument):
    template = models.CharField(max_length=255, blank=True, null=True, verbose_name="Template Name")
    parameters = models.JSONField(default=list, blank=True, null=True, verbose_name="Parameters")

class QualityFeedbackTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualityFeedbackTemplate
        fields = '__all__'

class QualityFeedbackTemplateViewSet(viewsets.ModelViewSet):
    queryset = QualityFeedbackTemplate.objects.all()
    serializer_class = QualityFeedbackTemplateSerializer

class QualityReviewObjective(BaseDocument):
    objective = models.TextField(blank=True, null=True, verbose_name="Objective")
    target = models.CharField(max_length=255, blank=True, null=True, verbose_name="Target")
    uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='UOM')
    review = models.TextField(blank=True, null=True, verbose_name="Review")
    status = models.CharField(max_length=255, choices=[('Open', 'Open'), ('Passed', 'Passed'), ('Failed', 'Failed')], blank=True, null=True, verbose_name='Status')

class QualityReviewObjectiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualityReviewObjective
        fields = '__all__'

class QualityReviewObjectiveViewSet(viewsets.ModelViewSet):
    queryset = QualityReviewObjective.objects.all()
    serializer_class = QualityReviewObjectiveSerializer

class QualityActionResolution(BaseDocument):
    problem = models.TextField(blank=True, null=True, verbose_name="Problem")
    resolution = models.TextField(blank=True, null=True, verbose_name="Resolution")
    status = models.CharField(max_length=255, choices=[('Open', 'Open'), ('Completed', 'Completed')], blank=True, null=True, verbose_name='Status')
    responsible = models.ForeignKey('erp_core.User', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Responsible')
    completion_by = models.DateField(blank=True, null=True, verbose_name="Completion By")

class QualityActionResolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualityActionResolution
        fields = '__all__'

class QualityActionResolutionViewSet(viewsets.ModelViewSet):
    queryset = QualityActionResolution.objects.all()
    serializer_class = QualityActionResolutionSerializer

class QualityFeedback(BaseDocument):
    template = models.ForeignKey('erp_core.QualityFeedbackTemplate', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Template')
    parameters = models.JSONField(default=list, blank=True, null=True, verbose_name="Parameters")
    document_type = models.CharField(max_length=255, choices=[('User', 'User'), ('Customer', 'Customer')], blank=True, null=True, verbose_name='Type')
    document_name = models.TextField(blank=True, null=True, verbose_name="Feedback By")

class QualityFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualityFeedback
        fields = '__all__'

class QualityFeedbackViewSet(viewsets.ModelViewSet):
    queryset = QualityFeedback.objects.all()
    serializer_class = QualityFeedbackSerializer

class QualityProcedure(BaseDocument):
    parent_quality_procedure = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Parent Procedure')
    is_group = models.BooleanField(default=False, verbose_name="Is Group")
    lft = models.IntegerField(default=0, verbose_name="Left Index")
    rgt = models.IntegerField(default=0, verbose_name="Right Index")
    old_parent = models.CharField(max_length=255, blank=True, null=True, verbose_name="old_parent")
    processes = models.JSONField(default=list, blank=True, null=True, verbose_name="Processes")
    quality_procedure_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Quality Procedure")
    process_owner = models.ForeignKey('erp_core.User', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Process Owner')
    process_owner_full_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Process Owner Full Name")

class QualityProcedureSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualityProcedure
        fields = '__all__'

class QualityProcedureViewSet(viewsets.ModelViewSet):
    queryset = QualityProcedure.objects.all()
    serializer_class = QualityProcedureSerializer

class QualityReview(BaseDocument):
    date = models.DateField(blank=True, null=True, verbose_name="Date")
    procedure = models.ForeignKey('erp_core.QualityProcedure', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Procedure')
    additional_information = models.TextField(blank=True, null=True, verbose_name="Additional Information")
    reviews = models.JSONField(default=list, blank=True, null=True, verbose_name="Reviews")
    status = models.CharField(max_length=255, choices=[('Open', 'Open'), ('Passed', 'Passed'), ('Failed', 'Failed')], blank=True, null=True, verbose_name='Status')
    goal = models.ForeignKey('erp_core.QualityGoal', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Goal')

class QualityReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualityReview
        fields = '__all__'

class QualityReviewViewSet(viewsets.ModelViewSet):
    queryset = QualityReview.objects.all()
    serializer_class = QualityReviewSerializer

class QualityMeetingAgenda(BaseDocument):
    agenda = models.TextField(blank=True, null=True, verbose_name="Agenda")

class QualityMeetingAgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualityMeetingAgenda
        fields = '__all__'

class QualityMeetingAgendaViewSet(viewsets.ModelViewSet):
    queryset = QualityMeetingAgenda.objects.all()
    serializer_class = QualityMeetingAgendaSerializer

class QualityMeetingMinutes(BaseDocument):
    minute = models.TextField(blank=True, null=True, verbose_name="Minute")
    document_type = models.CharField(max_length=255, choices=[('Quality Review', 'Quality Review'), ('Quality Action', 'Quality Action'), ('Quality Feedback', 'Quality Feedback')], blank=True, null=True, verbose_name='Document Type')
    document_name = models.TextField(blank=True, null=True, verbose_name="Document Name")

class QualityMeetingMinutesSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualityMeetingMinutes
        fields = '__all__'

class QualityMeetingMinutesViewSet(viewsets.ModelViewSet):
    queryset = QualityMeetingMinutes.objects.all()
    serializer_class = QualityMeetingMinutesSerializer

class QualityMeeting(BaseDocument):
    status = models.CharField(max_length=255, choices=[('Open', 'Open'), ('Closed', 'Closed')], blank=True, null=True, verbose_name='Status')
    minutes = models.JSONField(default=list, blank=True, null=True, verbose_name="Minutes")
    agenda = models.JSONField(default=list, blank=True, null=True, verbose_name="Agenda")

class QualityMeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualityMeeting
        fields = '__all__'

class QualityMeetingViewSet(viewsets.ModelViewSet):
    queryset = QualityMeeting.objects.all()
    serializer_class = QualityMeetingSerializer

class QualityGoalObjective(BaseDocument):
    objective = models.TextField(blank=True, null=True, verbose_name="Objective")
    target = models.CharField(max_length=255, blank=True, null=True, verbose_name="Target")
    uom = models.ForeignKey('erp_core.UOM', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='UOM')

class QualityGoalObjectiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualityGoalObjective
        fields = '__all__'

class QualityGoalObjectiveViewSet(viewsets.ModelViewSet):
    queryset = QualityGoalObjective.objects.all()
    serializer_class = QualityGoalObjectiveSerializer

class QualityFeedbackTemplateParameter(BaseDocument):
    parameter = models.CharField(max_length=255, blank=True, null=True, verbose_name="Parameter")

class QualityFeedbackTemplateParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualityFeedbackTemplateParameter
        fields = '__all__'

class QualityFeedbackTemplateParameterViewSet(viewsets.ModelViewSet):
    queryset = QualityFeedbackTemplateParameter.objects.all()
    serializer_class = QualityFeedbackTemplateParameterSerializer
