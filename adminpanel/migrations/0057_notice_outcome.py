# Generated by Django 5.0.1 on 2025-01-13 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0056_stock_exchange'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice_Outcome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice_outcome', models.FileField(upload_to='static/admin/img')),
                ('notice_outcome_details', models.CharField(max_length=100)),
            ],
        ),
    ]
