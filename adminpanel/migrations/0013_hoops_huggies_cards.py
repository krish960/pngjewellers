# Generated by Django 5.0.7 on 2025-01-06 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0012_hoops_huggies'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hoops_Huggies_cards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hoops_image', models.ImageField(upload_to='static/admin/img')),
                ('hoops_image_title', models.CharField(max_length=50)),
                ('hoops_latest_price', models.IntegerField()),
                ('hoops_old_price', models.IntegerField()),
            ],
        ),
    ]
