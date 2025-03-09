# Generated by Django 5.1.6 on 2025-03-08 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0003_menu_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='is_new',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='menu',
            name='is_promotion',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='ordermenu',
            name='order_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('discount_percentage', models.FloatField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('images', models.ImageField(upload_to='promotions/')),
                ('applicable_menu', models.ManyToManyField(to='pos.menu')),
            ],
        ),
    ]
