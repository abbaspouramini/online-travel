# Generated by Django 4.1.4 on 2022-12-25 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0005_remove_ticket_id_alter_ticket_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='train',
            name='isfull',
        ),
        migrations.RemoveField(
            model_name='train',
            name='remaining_capacity',
        ),
    ]
