# Generated by Django 3.1.7 on 2021-03-17 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20210317_0239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
