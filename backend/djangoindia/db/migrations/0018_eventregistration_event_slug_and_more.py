# Generated by Django 5.1.2 on 2024-10-27 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0017_alter_communitypartner_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventregistration',
            name='event_slug',
            field=models.SlugField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='communitypartner',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]