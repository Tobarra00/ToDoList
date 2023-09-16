# Generated by Django 4.2.5 on 2023-09-12 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='task_title',
            field=models.CharField(default='Test', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tasks',
            name='task_info',
            field=models.TextField(),
        ),
    ]
