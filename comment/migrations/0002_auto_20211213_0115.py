# Generated by Django 3.2.9 on 2021-12-13 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='budget',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='budget_amount',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='contacts',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='content_technical',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='cooperation',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='date',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='details',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='host',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='site_name',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='site_system',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='support',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='web_design',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='who_support',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='work_field',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='your_post',
        ),
    ]
