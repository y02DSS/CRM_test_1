# Generated by Django 3.2.9 on 2022-11-25 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0008_alter_task_home'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completedtask',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
