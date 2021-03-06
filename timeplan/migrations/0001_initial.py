# Generated by Django 2.2 on 2020-07-02 10:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Timeplan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='title', max_length=100)),
                ('describe', models.TextField()),
                ('differ', models.IntegerField(default=0)),
                ('num', models.IntegerField(default=1)),
                ('complete', models.BooleanField(default=False)),
                ('start', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('finish', models.DateTimeField(blank=True, default=None, null=True)),
                ('time', models.IntegerField(blank=True, default=0)),
                ('result', models.IntegerField(blank=True, default=0)),
                ('gb4', models.CharField(blank=True, max_length=1000)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ttitle', models.CharField(default='title', max_length=100)),
                ('tdescribe', models.TextField()),
                ('tdiffer', models.IntegerField(default=0)),
                ('tnum', models.IntegerField(default=1)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
