# Generated by Django 2.0.6 on 2019-05-23 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xmapp', '0005_auto_20190523_1533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='confirm_string',
            name='user',
        ),
        migrations.DeleteModel(
            name='confirm_string',
        ),
        migrations.DeleteModel(
            name='Mailbox',
        ),
    ]