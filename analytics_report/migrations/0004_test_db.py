# Generated by Django 3.0.4 on 2020-03-13 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics_report', '0003_auto_20200313_1221'),
    ]

    operations = [
        migrations.CreateModel(
            name='test_db',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature1', models.IntegerField(unique=True)),
                ('feature2', models.CharField(max_length=150)),
            ],
        ),
    ]