# Generated by Django 5.0.2 on 2024-05-11 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0014_rename_text_jobdetail_detail_of_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='professional',
            name='average_rating',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
    ]