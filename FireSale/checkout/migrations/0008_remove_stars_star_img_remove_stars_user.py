# Generated by Django 4.0.4 on 2022-05-10 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_remove_reviews_text_reviews_seller'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stars',
            name='star_img',
        ),
        migrations.RemoveField(
            model_name='stars',
            name='user',
        ),
    ]
