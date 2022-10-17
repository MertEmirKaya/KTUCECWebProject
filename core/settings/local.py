from core.settings.base import *


# DATABASES = {
#      'default': {
#          'ENGINE':'django.db.backends.postgresql_psycopg2',
#          'NAME':env('LOCAL_DATABASE_NAME'),
#          'USER':env('LOCAL_DATABASE_USER'),
#          'PASSWORD':env('LOCAL_DATABASE_PASS'),
#          'HOST':env('LOCAL_DATABASE_HOST'),
#          'PORT':'5432',
#      }
#  }
ALLOWED_HOSTS = ["*"]
MEDIA_ROOT= os.path.join(BASE_DIR,'media')
MEDIA_URL='/media/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# AWS_S3_ACCESS_KEY_ID=env("AWS_S3_ACCESS_KEY_ID")
# AWS_S3_SECRET_ACCESS_KEY=env("AWS_S3_SECRET_ACCESS_KEY")
# AWS_STORAGE_BUCKET_NAME=env("AWS_STORAGE_BUCKET_NAME")
# AWS_S3_FILE_OVERWRITE=False
# AWS_DEFAULT_ACL=None
# AWS_S3_REGION_NAME= "eu-central-1"
# AWS_S3_SIGNATURE_VERSION="s3v4"
# AWS_URL=os.environ.get('AWS_URL')
