# Generated by Django 3.1.7 on 2021-03-17 02:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='creat_at',
            new_name='create_at',
        ),
    ]
