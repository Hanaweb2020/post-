# Generated by Django 3.1.2 on 2020-11-11 09:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('BackendManagement', '0003_auto_20201109_0653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]