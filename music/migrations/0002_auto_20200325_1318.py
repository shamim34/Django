# Generated by Django 2.2.11 on 2020-03-25 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='fiel_type',
            new_name='file_type',
        ),
    ]