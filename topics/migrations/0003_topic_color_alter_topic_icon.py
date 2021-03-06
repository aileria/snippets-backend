# Generated by Django 4.0.2 on 2022-02-16 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0002_alter_topic_options_topic_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='color',
            field=models.CharField(default='', max_length=7),
        ),
        migrations.AlterField(
            model_name='topic',
            name='icon',
            field=models.ImageField(blank=True, upload_to='static/topics/'),
        ),
    ]
