# Generated by Django 4.2.9 on 2024-02-01 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=150)),
                ('logo', models.ImageField(upload_to='logo')),
                ('home_img', models.ImageField(upload_to='home_img')),
                ('confirm', models.ImageField(upload_to='confirm')),
                ('thanks', models.ImageField(upload_to='thanks')),
                ('video', models.FileField(upload_to='video')),
                ('p1', models.TextField()),
                ('p2', models.TextField()),
                ('p3', models.TextField()),
                ('p4', models.TextField()),
                ('copyright', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'CompanyProfile',
                'verbose_name_plural': 'CompanyProfile',
                'db_table': 'CompanyProfile',
                'managed': True,
            },
        ),
    ]
