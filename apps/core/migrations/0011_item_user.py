# Generated by Django 4.1.2 on 2022-10-31 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_remove_item_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='user',
            field=models.CharField(choices=[], max_length=200, null=True),
        ),
    ]
