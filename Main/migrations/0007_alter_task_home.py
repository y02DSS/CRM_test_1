# Generated by Django 3.2.9 on 2022-11-25 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0006_alter_task_home'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='home',
            field=models.CharField(choices=[('Дом 1', 'Дом 1'), ('Дом 2', 'Дом 2'), ('Дом 3', 'Дом 3')], max_length=200),
        ),
    ]