# Generated by Django 3.2.15 on 2022-09-26 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prjtapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prjttable',
            old_name='image',
            new_name='img',
        ),
    ]
