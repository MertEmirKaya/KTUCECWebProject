# Generated by Django 4.0.3 on 2022-03-30 12:27

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0004_textanswermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='BooleanAnswerModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.surveymodel')),
            ],
        ),
    ]
