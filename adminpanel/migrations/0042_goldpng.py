# Generated by Django 5.0.7 on 2025-01-10 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0041_goldplain'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoldPNG',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productImage', models.ImageField(upload_to='static/admin/img')),
                ('productTitle', models.CharField(max_length=200)),
                ('latestPrice', models.IntegerField()),
                ('oldPrice', models.IntegerField()),
            ],
        ),
    ]
