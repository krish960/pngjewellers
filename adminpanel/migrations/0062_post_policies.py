# Generated by Django 5.0.1 on 2025-01-13 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0061_risk_policies'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post_Policies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_policies', models.FileField(upload_to='static/admin/img')),
                ('post_policies_details', models.CharField(max_length=100)),
            ],
        ),
    ]
