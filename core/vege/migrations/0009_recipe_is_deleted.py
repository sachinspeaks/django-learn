# Generated by Django 4.2.4 on 2023-09-20 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0008_alter_reportcard_date_of_report_card_generation'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]