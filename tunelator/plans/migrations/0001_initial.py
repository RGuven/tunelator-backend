# Generated by Django 3.2 on 2022-04-02 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='name')),
                ('description', models.TextField(verbose_name='description')),
            ],
            options={
                'verbose_name': 'plan',
                'verbose_name_plural': 'plans',
            },
        ),
        migrations.CreateModel(
            name='PlanConfigurationItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='configs', to='plans.plan', verbose_name='plan')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_plans.planconfigurationitem_set+', to='contenttypes.contenttype')),
            ],
            options={
                'verbose_name': 'plan configuration item',
                'verbose_name_plural': 'plan configuration items',
            },
        ),
        migrations.CreateModel(
            name='PlanConfigurationBooleanItem',
            fields=[
                ('planconfigurationitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='plans.planconfigurationitem')),
                ('value', models.BooleanField(default=True, verbose_name='value')),
            ],
            options={
                'verbose_name': 'plan configuration boolean item',
                'verbose_name_plural': 'plan configuration boolean items',
            },
            bases=('plans.planconfigurationitem',),
        ),
        migrations.CreateModel(
            name='PlanConfigurationStringItem',
            fields=[
                ('planconfigurationitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='plans.planconfigurationitem')),
                ('value', models.CharField(blank=True, default='', max_length=150, verbose_name='value')),
            ],
            options={
                'verbose_name': 'plan configuration string item',
                'verbose_name_plural': 'plan configuration string items',
            },
            bases=('plans.planconfigurationitem',),
        ),
        migrations.CreateModel(
            name='PlanDisplayFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=True, verbose_name='enabled')),
                ('name', models.CharField(max_length=150, verbose_name='name')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='display_features', to='plans.plan', verbose_name='plan')),
            ],
            options={
                'verbose_name': 'plan display feature',
                'verbose_name_plural': 'plan display features',
            },
        ),
    ]
