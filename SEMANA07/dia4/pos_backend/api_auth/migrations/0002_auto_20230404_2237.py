# Generated by Django 3.2 on 2023-04-05 03:37

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api_auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_foto', cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='image')),
                ('emp_tipo', models.CharField(max_length=20)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tbl_empleado',
            },
        ),
        migrations.DeleteModel(
            name='AuthUser',
        ),
    ]
