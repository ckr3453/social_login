# Generated by Django 2.1.5 on 2019-03-01 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s_login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pictures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
