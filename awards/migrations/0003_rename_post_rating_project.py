# Generated by Django 3.2.8 on 2021-10-27 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0002_auto_20211026_0525'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='post',
            new_name='project',
        ),
    ]
