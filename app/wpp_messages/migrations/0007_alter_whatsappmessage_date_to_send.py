# Generated by Django 3.2.6 on 2022-09-29 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wpp_messages', '0006_auto_20220927_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='whatsappmessage',
            name='date_to_send',
            field=models.DateField(null=True, verbose_name='Date to Send'),
        ),
    ]