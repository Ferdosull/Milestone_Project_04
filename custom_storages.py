from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


# Cloud storage location for static files using AWS
class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


# Cloud storage location for media files using AWS
class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
