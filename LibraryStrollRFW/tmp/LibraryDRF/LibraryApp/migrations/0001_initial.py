# Generated by Django 4.2 on 2023-04-10 03:52

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('describe', models.TextField(blank=True)),
                ('photo', models.ImageField(blank=True, upload_to='IMG')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('rating', models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0, null=True)),
                ('date_create', models.DateField(default=datetime.datetime.now)),
                ('published_date', models.DateField()),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='LibraryApp.author')),
            ],
        ),
        migrations.CreateModel(
            name='UserBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('planned', 'Запланированная книга'), ('read', 'Прочитанная книга')], max_length=20)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='LibraryApp.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]