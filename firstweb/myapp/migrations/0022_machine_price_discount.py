# Generated by Django 5.1.6 on 2025-02-28 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_alter_comments_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='machine',
            name='price_discount',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
