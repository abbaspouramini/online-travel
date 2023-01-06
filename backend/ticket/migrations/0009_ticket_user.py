# Generated by Django 4.1.4 on 2022-12-25 21:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ticket', '0008_alter_trip_remaining_capacity'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usertickets', to=settings.AUTH_USER_MODEL),
        ),
    ]
