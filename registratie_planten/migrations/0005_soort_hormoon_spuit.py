# Generated by Django 5.1.2 on 2024-10-21 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registratie_planten', '0004_alter_tripsinfestationweek10_oppot_week_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='soort',
            name='hormoon_spuit',
            field=models.DecimalField(decimal_places=2, help_text='Percentage value (0.00 - 100.00)', max_digits=5, null=True),
        ),
    ]
