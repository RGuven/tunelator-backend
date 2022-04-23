# Generated by Django 3.2 on 2022-04-23 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0008_plan_stripe_price_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='approval',
            name='approval_id',
        ),
        migrations.AddField(
            model_name='approval',
            name='stripe_session_id',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='stripe session id'),
        ),
        migrations.AddField(
            model_name='approval',
            name='stripe_subscription_id',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='stripe subscription id'),
        ),
        migrations.AlterField(
            model_name='approval',
            name='status',
            field=models.CharField(choices=[('active', 'active'), ('past_due', 'past due'), ('unpaid', 'unpaid'), ('canceled', 'canceled'), ('incomplete', 'incomplete'), ('incomplete_expired', 'incomplete expired'), ('trialing', 'trialing')], default='incomplete', max_length=50, verbose_name='status'),
        ),
    ]
