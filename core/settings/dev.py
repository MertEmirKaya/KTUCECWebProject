from core.settings.base import *

DATABASES = {
     'default': {
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME':os.environ.get('DATABASE_NAME'),
        'USER':os.environ.get('DATABASE_USER'),
        'PASSWORD':os.environ.get('DATABASE_PASS'),
        'HOST':'ec2-52-48-159-67.eu-west-1.compute.amazonaws.com',
        'PORT':'5432',
     }
 }

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_S3_ACCESS_KEY_ID=os.environ.get('AWS_S3_ACCESS_KEY_ID'),
AWS_S3_SECRET_ACCESS_KEY=os.environ.get('AWS_S3_SECRET_ACCESS_KEY'),
AWS_STORAGE_BUCKET_NAME=os.environ.get('AWS_STORAGE_BUCKET_NAME'),
AWS_URL=os.environ.get('AWS_URL')
AWS_QUERYSTRING_AUTH=False

STATIC_URL = AWS_URL + '/static/'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
MEDIA_URL = AWS_URL + '/media/'
