# Generated by Django 5.0.7 on 2025-01-06 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0015_hoops_question_ans'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hoops_question_ans',
            name='answer',
        ),
    ]
