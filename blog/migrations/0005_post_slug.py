# Generated by Django 5.0.1 on 2024-01-25 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(default=' ', max_length=140),
            preserve_default=False,
        ),
    ]
