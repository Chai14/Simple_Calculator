# Generated by Django 4.2.3 on 2023-07-29 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_title', models.CharField(max_length=50)),
                ('service_operations', models.CharField(max_length=50)),
                ('service_des', models.TextField()),
            ],
        ),
    ]