# Generated by Django 3.1 on 2020-09-23 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField(max_length=300)),
                ('resource_title', models.CharField(max_length=150)),
                ('resource_description', models.TextField()),
                ('resource_url', models.URLField(max_length=300)),
            ],
        ),
    ]
