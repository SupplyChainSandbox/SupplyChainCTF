# Generated by Django 3.0.5 on 2020-07-16 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_vendor_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='system',
            name='downtime_cost',
            field=models.IntegerField(default=0, help_text='Downtime to set up '),
        ),
        migrations.AddField(
            model_name='system',
            name='setup_cost',
            field=models.IntegerField(default=0, help_text='Cost in score it takes to set this baby up'),
        ),
        migrations.AddField(
            model_name='vendor',
            name='downtime_cost_multiplier',
            field=models.FloatField(default=1.0),
        ),
        migrations.AddField(
            model_name='vendor',
            name='setup_cost_multiplier',
            field=models.FloatField(default=1.0),
        ),
        migrations.AlterField(
            model_name='systemstate',
            name='active_tags',
            field=models.ManyToManyField(blank=True, to='game.Tag'),
        ),
    ]
