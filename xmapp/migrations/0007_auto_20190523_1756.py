# Generated by Django 2.0.6 on 2019-05-23 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('xmapp', '0006_auto_20190523_1537'),
    ]

    operations = [
        migrations.CreateModel(
            name='confirm_string',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=256, verbose_name='用户注册码')),
                ('code_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 't_confirm_string',
            },
        ),
        migrations.AlterModelOptions(
            name='torderitem',
            options={},
        ),
        migrations.AlterModelOptions(
            name='tuser',
            options={},
        ),
        migrations.AddField(
            model_name='confirm_string',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xmapp.TUser', verbose_name='关联的用户'),
        ),
    ]
