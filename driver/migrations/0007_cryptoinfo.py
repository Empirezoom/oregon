# Generated by Django 4.2.9 on 2024-02-02 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0006_thanksedit'),
    ]

    operations = [
        migrations.CreateModel(
            name='CryptoInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=5000)),
                ('scan', models.ImageField(upload_to='crypto')),
                ('time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'scan to pay',
                'verbose_name_plural': 'scan to pays',
                'db_table': 'scan to pay',
                'managed': True,
            },
        ),
    ]
