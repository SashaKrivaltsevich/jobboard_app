# Generated by Django 4.2.3 on 2023-07-22 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_vacancy_attachment'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='logo',
            field=models.ImageField(null=True, upload_to='companies/logo'),
        ),
    ]
