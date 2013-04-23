from django.db import models


class UploadCategory(models.Model):
    name = models.CharField(max_length=255)


class UploadedFile(models.Model):
    category = models.ForeignKey(UploadCategory)
    filename = models.CharField(max_length=255)
    release_notes = models.TextField()
    major_version = models.IntegerField()
    minor_version = models.IntegerField()
    version_letter = models.CharField(max_length=2)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
