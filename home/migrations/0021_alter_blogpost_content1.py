# Generated by Django 4.0.4 on 2022-04-23 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_alter_blogpost_content1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='content1',
            field=models.TextField(blank=True, null=True),
        ),
    ]
