# Generated by Django 4.2.16 on 2025-05-14 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0008_alter_store_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='loc',
        ),
    ]
