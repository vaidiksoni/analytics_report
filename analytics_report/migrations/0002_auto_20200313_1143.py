# Generated by Django 3.0.4 on 2020-03-13 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analytics_report', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='analytics_report.ratings'),
        ),
    ]