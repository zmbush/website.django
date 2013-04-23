from django.contrib import admin
from users.models import UploadCategory, UploadedFile

admin.site.register(UploadCategory)
admin.site.register(UploadedFile)
