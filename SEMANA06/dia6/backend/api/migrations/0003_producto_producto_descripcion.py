# Generated by Django 3.2 on 2023-04-01 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_producto_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='producto_descripcion',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
