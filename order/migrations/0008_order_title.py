# Generated by Django 4.2.3 on 2023-07-20 21:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0007_order_ready_cake"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="title",
            field=models.CharField(
                blank=True, max_length=90, null=True, verbose_name="Название торта"
            ),
        ),
    ]
