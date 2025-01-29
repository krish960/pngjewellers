# Generated by Django 5.0.1 on 2025-01-13 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0050_corporate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_companies', models.FileField(upload_to='static/admin/img')),
                ('group_companies_details', models.CharField(max_length=100)),
            ],
        ),
    ]
