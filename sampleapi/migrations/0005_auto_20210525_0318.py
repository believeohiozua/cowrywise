# Generated by Django 3.0 on 2021-05-25 03:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sampleapi', '0004_auto_20210525_0254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uuidgenerator',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]
