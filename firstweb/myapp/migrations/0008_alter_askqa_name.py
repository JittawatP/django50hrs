# Generated by Django 5.1.6 on 2025-02-14 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_askqa_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='askqa',
            name='name',
            field=models.CharField(max_length=100, verbose_name='ชื่อ'),
        ),
    ]
