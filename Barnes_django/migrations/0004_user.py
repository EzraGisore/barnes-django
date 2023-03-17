# Generated by Django 4.1.7 on 2023-03-08 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Barnes_django', '0003_alter_member_regid'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('gender', models.CharField(blank=True, max_length=50)),
                ('age', models.IntegerField(blank=True, max_length=50)),
                ('email', models.EmailField(blank=True, max_length=50)),
                ('phone', models.CharField(blank=True, max_length=50)),
                ('regID', models.CharField(blank=True, max_length=50)),
                ('membership', models.CharField(blank=True, max_length=50)),
                ('password', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]