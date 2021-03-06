# Generated by Django 4.0.4 on 2022-05-05 10:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0004_item_priceidea_alter_offers_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='seller',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='offers',
            name='buyer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
