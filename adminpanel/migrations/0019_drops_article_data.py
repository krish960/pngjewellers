# Generated by Django 5.0.7 on 2025-01-06 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0018_drops_card_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drops_Article_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hoops_articleHeading', models.CharField(max_length=100)),
                ('hoops_articleDescription', models.CharField(max_length=1000)),
            ],
        ),
    ]
