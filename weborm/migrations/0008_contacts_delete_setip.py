# Generated by Django 5.1.2 on 2024-11-06 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weborm', '0007_serverip'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('address', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='SetIP',
        ),
    ]