# Generated by Django 4.2.9 on 2024-02-02 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0007_cryptoinfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cryptoinfo',
            old_name='text',
            new_name='wallet_address',
        ),
        migrations.AddField(
            model_name='cryptoinfo',
            name='types',
            field=models.CharField(default='ir', max_length=50),
        ),
    ]
