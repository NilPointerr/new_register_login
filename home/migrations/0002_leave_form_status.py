# Generated by Django 4.1.7 on 2023-04-03 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave_form',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Cancle', 'Cancle')], default='Pending', max_length=100),
        ),
    ]