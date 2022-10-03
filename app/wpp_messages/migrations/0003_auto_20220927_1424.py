# Generated by Django 3.2.6 on 2022-09-27 14:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wpp_messages', '0002_alter_whatsappmessage_to'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='whatsappmessage',
            options={'verbose_name': 'Message', 'verbose_name_plural': 'Messages'},
        ),
        migrations.RenameField(
            model_name='whatsappmessage',
            old_name='system',
            new_name='consumer_system',
        ),
        migrations.AddField(
            model_name='whatsappmessage',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='whatsappmessage',
            name='date_to_send',
            field=models.DateTimeField(verbose_name='Date to Send'),
        ),
    ]