# Generated by Django 2.2 on 2019-04-25 22:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('libraryapp', '0003_auto_20190425_2053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='checked_out',
        ),
        migrations.CreateModel(
            name='BookCheckout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_checkout', models.DateTimeField(auto_now_add=True)),
                ('date_checkin', models.DateTimeField(blank=True, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='checkouts', to='libraryapp.Book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='checkouts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
