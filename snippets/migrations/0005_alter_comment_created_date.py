# Generated by Django 4.0.2 on 2022-02-19 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0004_alter_snippet_description_alter_snippet_topics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]