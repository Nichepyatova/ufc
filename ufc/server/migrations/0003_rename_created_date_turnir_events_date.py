# Generated by Django 4.1.6 on 2023-02-08 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_alter_turnir_created_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='turnir',
            old_name='created_date',
            new_name='events_date',
        ),
    ]
