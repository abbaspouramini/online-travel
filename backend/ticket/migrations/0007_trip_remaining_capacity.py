# Generated by Django 4.1.4 on 2022-12-25 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0006_remove_train_isfull_remove_train_remaining_capacity'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='remaining_capacity',
            field=models.IntegerField(default=0),
        ),
    ]
