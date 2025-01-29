# Generated by Django 5.0.7 on 2025-01-09 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0039_aaryas_arrival_goldjewellery_bestseller_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gold_GoldBraceletss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gold_GoldBracelets_image', models.ImageField(upload_to='static/admin/img')),
                ('Gold_GoldBracelets_image_title', models.CharField(max_length=200)),
                ('Gold_GoldBracelets_latest_price', models.IntegerField()),
                ('Gold_GoldBracelets_old_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Gold_Jhumkass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gold_Jhumkas_image', models.ImageField(upload_to='static/admin/img')),
                ('Gold_Jhumkas_image_title', models.CharField(max_length=200)),
                ('Gold_Jhumkas_latest_price', models.IntegerField()),
                ('Gold_Jhumkas_old_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Gold_Menstuds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gold_Menstuds_image', models.ImageField(upload_to='static/admin/img')),
                ('Gold_Menstuds_image_title', models.CharField(max_length=200)),
                ('Gold_Menstuds_latest_price', models.IntegerField()),
                ('Gold_Menstuds_old_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Gold_vedhani',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gold_vedhani_image', models.ImageField(upload_to='static/admin/img')),
                ('Gold_vedhani_image_title', models.CharField(max_length=200)),
                ('Gold_vedhani_latest_price', models.IntegerField()),
                ('Gold_vedhani_old_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='KurtaPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Kurta_image', models.ImageField(upload_to='static/admin/img')),
                ('Kurta_title', models.CharField(max_length=200)),
                ('Kurta_latest_price', models.IntegerField()),
                ('Kurta_old_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Mangalsutra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mangalsutra_image', models.ImageField(upload_to='static/admin/img')),
                ('mangalsutra_title', models.CharField(max_length=200)),
                ('mangalsutra_Latest_price', models.IntegerField()),
                ('mangalsutra_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Mangalsutras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Mangalsutra_articleHeading', models.CharField(max_length=100)),
                ('Mangalsutra_articleDescription', models.CharField(max_length=200)),
            ],
        ),
    ]
