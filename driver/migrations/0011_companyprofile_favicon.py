# Generated by Django 4.2.9 on 2024-02-02 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0010_bnbinfo_btcinfo_dogeinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyprofile',
            name='favicon',
            field=models.ImageField(default='favicon.jpg', upload_to='logo'),
        ),
    ]
