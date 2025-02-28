# Generated by Django 5.1.6 on 2025-02-27 07:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_orderproduct_profile_cart_quantity_cart_cartorder'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('year', models.CharField(max_length=4)),
                ('machine_type', models.CharField(choices=[('cnd', 'CNC'), ('lathe', 'เครื่องกลึง'), ('milling', 'เครื่องกัด'), ('gear milling', 'เครื่องไสเฟือง')], default='CNC', max_length=100)),
                ('images', models.ImageField(blank=True, null=True, upload_to='machines')),
                ('price_per_day', models.IntegerField(default=0)),
                ('earnest_money', models.IntegerField(blank=True, default=1000, null=True)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.machine')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_card', models.CharField(max_length=13)),
                ('customer_name', models.CharField(max_length=50)),
                ('tel', models.CharField(max_length=11)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('rental_price', models.IntegerField(default=0)),
                ('total_rental_price', models.IntegerField(default=0)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.machine')),
            ],
        ),
    ]
