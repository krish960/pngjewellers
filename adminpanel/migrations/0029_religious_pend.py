# Generated by Django 5.0.7 on 2025-01-08 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0028_heartpendant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Religious_Pend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productImage', models.ImageField(upload_to='static/admin/img')),
                ('productTitle', models.CharField(max_length=200)),
                ('latestPrice', models.IntegerField()),
                ('oldPrice', models.IntegerField()),
            ],
        ),
    ]
