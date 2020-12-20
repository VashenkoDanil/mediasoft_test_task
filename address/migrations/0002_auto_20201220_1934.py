# Generated by Django 3.1.4 on 2020-12-20 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='address',
            unique_together={('street', 'house')},
        ),
        migrations.AlterUniqueTogether(
            name='streets',
            unique_together={('name', 'city')},
        ),
    ]
