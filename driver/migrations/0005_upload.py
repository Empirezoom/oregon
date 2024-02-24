# Generated by Django 4.2.9 on 2024-02-02 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0004_application'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screenshot', models.ImageField(upload_to='payment screenshot')),
                ('uploaded', models.CharField(default='screenshot', max_length=50)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'upload',
                'verbose_name_plural': 'uploads',
                'db_table': 'upload',
                'managed': True,
            },
        ),
    ]