from django.db import models
from erp_core.models import BaseDocument
from rest_framework import serializers, viewsets

class PortalUser(BaseDocument):
    user = models.ForeignKey('erp_core.User', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='User')

class PortalUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortalUser
        fields = '__all__'

class PortalUserViewSet(viewsets.ModelViewSet):
    queryset = PortalUser.objects.all()
    serializer_class = PortalUserSerializer

class Video(BaseDocument):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Title")
    provider = models.CharField(max_length=255, choices=[('YouTube', 'YouTube'), ('Vimeo', 'Vimeo')], blank=True, null=True, verbose_name='Provider')
    url = models.CharField(max_length=255, blank=True, null=True, verbose_name="URL")
    publish_date = models.DateField(blank=True, null=True, verbose_name="Publish Date")
    duration = models.TextField(blank=True, null=True, verbose_name="Duration")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    like_count = models.FloatField(default=0.0, verbose_name="Likes")
    view_count = models.FloatField(default=0.0, verbose_name="Views")
    dislike_count = models.FloatField(default=0.0, verbose_name="Dislikes")
    comment_count = models.FloatField(default=0.0, verbose_name="Comments")
    image = models.ImageField(upload_to='uploads/', blank=True, null=True, verbose_name="Image")
    youtube_video_id = models.CharField(max_length=255, blank=True, null=True, verbose_name="Youtube ID")

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class VideoSettings(BaseDocument):
    enable_youtube_tracking = models.BooleanField(default=False, verbose_name="Enable YouTube Tracking")
    api_key = models.CharField(max_length=255, blank=True, null=True, verbose_name="API Key")
    frequency = models.CharField(max_length=255, choices=[('30 mins', '30 mins'), ('1 hr', '1 hr'), ('6 hrs', '6 hrs'), ('Daily', 'Daily')], blank=True, null=True, verbose_name='Frequency')

class VideoSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoSettings
        fields = '__all__'

class VideoSettingsViewSet(viewsets.ModelViewSet):
    queryset = VideoSettings.objects.all()
    serializer_class = VideoSettingsSerializer

class RenameTool(BaseDocument):
    select_doctype = models.ForeignKey('erp_core.DocType', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Select DocType')
    file_to_rename = models.FileField(upload_to='uploads/', blank=True, null=True, verbose_name="File to Rename")

class RenameToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = RenameTool
        fields = '__all__'

class RenameToolViewSet(viewsets.ModelViewSet):
    queryset = RenameTool.objects.all()
    serializer_class = RenameToolSerializer
