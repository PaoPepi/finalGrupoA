# Generated by Django 4.0 on 2022-02-10 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_biblioteca', '0018_alter_comentarios_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]
