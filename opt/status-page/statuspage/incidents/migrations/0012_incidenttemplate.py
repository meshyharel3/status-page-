# Generated by Django 4.1.7 on 2023-03-12 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0005_component_show_historic_incidents'),
        ('incidents', '0011_alter_incidentupdate_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='IncidentTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('title', models.CharField(max_length=255)),
                ('visibility', models.BooleanField(default=False)),
                ('template_name', models.CharField(max_length=255)),
                ('status', models.CharField(default='investigating', max_length=255)),
                ('impact', models.CharField(default='none', max_length=255)),
                ('update_component_status', models.BooleanField(default=False)),
                ('text', models.CharField(max_length=65536)),
                ('components', models.ManyToManyField(blank=True, related_name='+', to='components.component')),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
    ]
