# Generated by Django 3.2 on 2022-06-17 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contact_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='responded',
            field=models.BooleanField(null=True),
        ),
    ]
