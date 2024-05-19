# Generated by Django 5.0.4 on 2024-05-19 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0011_alter_election_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='SentEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.EmailField(max_length=254)),
                ('recipient', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('reply_to', models.EmailField(blank=True, max_length=254, null=True)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]