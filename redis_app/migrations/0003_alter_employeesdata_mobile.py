# Generated by Django 5.0.7 on 2024-07-20 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redis_app', '0002_alter_employeesdata_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeesdata',
            name='mobile',
            field=models.CharField(max_length=255),
        ),
    ]