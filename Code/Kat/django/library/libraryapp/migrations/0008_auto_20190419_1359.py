# Generated by Django 2.2 on 2019-04-19 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0007_remove_book_checked_out'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='author',
            new_name='name',
        ),
    ]
