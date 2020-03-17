# Generated by Django 3.0.4 on 2020-03-17 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=15)),
                ('description', models.TextField()),
                ('date_added', models.DateTimeField()),
                ('stock', models.IntegerField()),
            ],
        ),
    ]