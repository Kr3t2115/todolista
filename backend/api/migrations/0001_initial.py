# Generated by Django 4.0.3 on 2022-05-30 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='todoModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('isCompleted', models.BooleanField()),
            ],
        ),
    ]
