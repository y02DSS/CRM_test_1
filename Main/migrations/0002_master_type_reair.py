# Generated by Django 3.2.9 on 2022-11-24 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='master',
            name='type_reair',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='Main.typerepair'),
            preserve_default=False,
        ),
    ]
