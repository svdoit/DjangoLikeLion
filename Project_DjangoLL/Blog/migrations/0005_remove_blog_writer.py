# Generated by Django 3.1.1 on 2020-09-19 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_blog_writer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='writer',
        ),
    ]
