# Generated by Django 2.2 on 2019-04-18 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0002_auto_20190418_1418'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='author',
            new_name='author_text',
        ),
    ]
