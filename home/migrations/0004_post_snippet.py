# Generated by Django 3.2 on 2021-04-26 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='This is Short Info About Blog', max_length=255),
        ),
    ]
