# Generated by Django 4.0.2 on 2022-03-30 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0013_alter_yearlyresult_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yearlyresult',
            name='comments',
            field=models.CharField(blank=True, choices=[('Poor', 'Poor'), ('Bellow Average', 'Bellow Average'), ('Excellent', 'Excellent'), ('Very Good', 'Very Good'), ('Average', 'Average'), ('Good', 'Good')], max_length=50, null=True),
        ),
    ]