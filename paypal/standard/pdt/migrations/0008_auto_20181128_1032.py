# Generated by Django 2.1.3 on 2018-11-28 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pdt", "0007_auto_20160219_1137"),
    ]

    operations = [
        migrations.AlterField(
            model_name="paypalpdt",
            name="flag",
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name="paypalpdt",
            name="test_ipn",
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
