# Generated by Django 3.2.16 on 2022-11-17 20:09

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_user_is_online'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_image',
            field=models.ImageField(blank=True, default='https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png', null=True, upload_to=core.models.post_image_file_path),
        ),
    ]