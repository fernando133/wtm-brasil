# Generated by Django 3.2.6 on 2022-09-30 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wpp_messages', '0007_alter_whatsappmessage_date_to_send'),
    ]

    operations = [
        migrations.AddField(
            model_name='whatsappmessage',
            name='api_return',
            field=models.TextField(max_length=500, null=True, verbose_name='Graph Api Return'),
        ),
    ]
