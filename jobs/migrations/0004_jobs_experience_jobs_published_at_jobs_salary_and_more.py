# Generated by Django 4.2.5 on 2023-10-02 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_jobs_description_alter_jobs_job_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='experience',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='jobs',
            name='published_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='jobs',
            name='salary',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='jobs',
            name='vacancy',
            field=models.IntegerField(default=1),
        ),
    ]
