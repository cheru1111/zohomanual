# Generated by Django 4.2.3 on 2023-11-13 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0004_alter_journal_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('save', 'Save')], max_length=10),
        ),
    ]
