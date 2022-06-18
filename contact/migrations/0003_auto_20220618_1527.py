# Generated by Django 3.2 on 2022-06-18 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20220618_1305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='month',
        ),
        migrations.AddField(
            model_name='contact',
            name='reason',
            field=models.CharField(choices=[('1', 'Dive Equipment Shop / Online Orders'), ('2', 'Diving Courses'), ('3', 'General Enquiry')], default='1', max_length=2),
        ),
    ]
