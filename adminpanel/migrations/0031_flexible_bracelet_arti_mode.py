# Generated by Django 5.0.7 on 2025-01-08 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0030_flexible_brac_card'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flexible_Bracelet_arti_mode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articleHeading', models.CharField(max_length=200)),
                ('articleDescription', models.CharField(max_length=1300)),
            ],
        ),
    ]
