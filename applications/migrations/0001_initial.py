# Generated by Django 2.2.3 on 2019-08-06 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('destination', models.CharField(max_length=150)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
