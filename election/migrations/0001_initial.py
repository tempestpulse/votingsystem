# Generated by Django 5.0.4 on 2024-04-03 22:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Election',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('max_candidates_choice', models.PositiveIntegerField(default=1)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('creation_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('vote_count', models.IntegerField(default=0)),
                ('election', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='election.election')),
                ('party', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='election.party')),
            ],
        ),
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('election', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='election.election')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chosen_candidates', models.ManyToManyField(related_name='votes', to='election.candidate')),
                ('election', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='election.election')),
                ('voter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='election.voter')),
            ],
        ),
    ]
