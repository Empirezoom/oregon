# Generated by Django 4.2.9 on 2024-02-01 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0003_applicationchoice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('address', models.CharField(max_length=500)),
                ('sent', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'application form',
                'verbose_name_plural': 'application form',
                'db_table': 'application form',
                'managed': True,
            },
        ),
    ]
