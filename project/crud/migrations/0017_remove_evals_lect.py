# Generated by Django 3.0.1 on 2020-02-21 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0016_evals_lect'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evals',
            name='lect',
        ),
    ]
