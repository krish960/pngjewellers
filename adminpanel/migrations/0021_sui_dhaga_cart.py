# Generated by Django 5.0.7 on 2025-01-07 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0020_drops_question_ans_alter_hoops_question_ans_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sui_Dhaga_cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productImage', models.ImageField(upload_to='static/admin/img')),
                ('productTitle', models.CharField(max_length=200)),
                ('latestPrice', models.IntegerField()),
                ('oldPrice', models.IntegerField()),
            ],
        ),
    ]
