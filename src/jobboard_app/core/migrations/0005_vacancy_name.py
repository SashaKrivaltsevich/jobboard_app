# Generated by Django 4.2.3 on 2023-07-17 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_populate_levels_table_with_defaults'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='name',
            field=models.CharField(default='Test value', max_length=100),
            preserve_default=False,
        ),
    ]