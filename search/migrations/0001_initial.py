# Generated by Django 5.0.3 on 2024-04-28 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='vulnerability_detail',
            fields=[
                ('cve_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('cvss_score', models.DecimalField(decimal_places=2, max_digits=3)),
                ('description', models.TextField()),
                ('published_date', models.CharField(max_length=100)),
                ('base_severity', models.CharField(max_length=100)),
                ('mitigations', models.TextField()),
            ],
            options={
                'db_table': 'vulnerabilities',
                'managed': False,
            },
        ),
    ]
