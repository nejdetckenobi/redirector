# Generated by Django 2.2.1 on 2019-05-29 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redirections', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='redirection',
            name='is_permanent',
            field=models.BooleanField(default=False),
        ),
    ]
