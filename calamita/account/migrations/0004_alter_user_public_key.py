# Generated by Django 4.1.7 on 2023-03-26 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='public_key',
            field=models.CharField(max_length=500, unique=True),
        ),
    ]
