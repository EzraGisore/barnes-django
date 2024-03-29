# Generated by Django 4.2.3 on 2023-11-06 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Barnes_django', '0006_delete_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('gender', models.CharField(blank=True, max_length=50)),
                ('age', models.IntegerField(blank=True, max_length=50)),
                ('email', models.EmailField(blank=True, max_length=50)),
                ('phone', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='BcMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('gender', models.CharField(blank=True, max_length=50)),
                ('age', models.IntegerField(blank=True, max_length=50)),
                ('email', models.EmailField(blank=True, max_length=50)),
                ('phone', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='JrMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_name', models.CharField(blank=True, max_length=50)),
                ('junior_name', models.CharField(blank=True, max_length=50)),
                ('gender', models.CharField(blank=True, max_length=50)),
                ('age', models.IntegerField(blank=True, max_length=50)),
                ('parent_email', models.EmailField(blank=True, max_length=50)),
                ('parent_phone', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
