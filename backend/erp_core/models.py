from django.db import models
from django.conf import settings

class BaseDocument(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="%(class)s_owner")
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="%(class)s_modified_by")
    creation = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    docstatus = models.IntegerField(default=0)
    idx = models.IntegerField(default=0)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.before_save()
        self.validate()
        super().save(*args, **kwargs)
        self.on_update()

    def before_save(self):
        pass

    def validate(self):
        pass

    def on_update(self):
        pass
