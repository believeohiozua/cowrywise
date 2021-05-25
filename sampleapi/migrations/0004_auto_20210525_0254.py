# Generated by Django 3.0 on 2021-05-25 02:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sampleapi', '0003_auto_20210525_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uuidgenerator',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
