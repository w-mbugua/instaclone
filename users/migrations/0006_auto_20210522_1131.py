# Generated by Django 3.2.3 on 2021-05-22 08:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0005_image_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='Likes',
            field=models.ManyToManyField(blank=True, related_name='images_liked', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='image',
            name='comments',
            field=models.ManyToManyField(blank=True, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
    ]
