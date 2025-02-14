# Generated by Django 5.0.7 on 2025-01-06 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0017_drops_banner_img1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drops_Card_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hoops_image', models.ImageField(upload_to='static/admin/img')),
                ('hoops_image_title', models.CharField(max_length=50)),
                ('hoops_latest_price', models.IntegerField()),
                ('hoops_old_price', models.IntegerField()),
            ],
        ),
    ]
