# Generated by Django 4.0.2 on 2022-03-20 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0005_alter_yearlyresult_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yearlyresult',
            name='comments',
            field=models.CharField(blank=True, choices=[('Very Good', 'Very Good'), ('Excellent', 'Excellent'), ('Average', 'Average'), ('Bellow Average', 'Bellow Average'), ('Poor', 'Poor'), ('Good', 'Good')], max_length=50, null=True),
        ),
    ]