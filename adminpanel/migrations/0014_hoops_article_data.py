# Generated by Django 5.0.7 on 2025-01-06 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0013_hoops_huggies_cards'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hoops_Article_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hoops_articleHeading', models.CharField(max_length=100)),
                ('hoops_articleDescription', models.CharField(max_length=1000)),
            ],
        ),
    ]
