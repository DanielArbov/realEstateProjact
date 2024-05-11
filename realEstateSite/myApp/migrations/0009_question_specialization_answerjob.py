# Generated by Django 5.0.2 on 2024-02-22 18:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0008_alter_answer_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='specialization',
            field=models.CharField(choices=[('CONTRACTOR', 'contractor'), ('ARCHITECT', 'architect'), ('SUPERVISOR', 'supervisor'), ('DESIGNER', 'interior designer')], default='Specialization.CONTRACTOR', max_length=20),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='AnswerJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_value', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('jobDetail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.jobdetail')),
                ('question', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myApp.question')),
            ],
        ),
    ]