# Generated by Django 4.2.9 on 2024-02-03 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0012_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyprofile',
            name='notification',
            field=models.ImageField(default='notification.jpg', upload_to='logo'),
        ),
    ]