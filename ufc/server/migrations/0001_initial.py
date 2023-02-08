# Generated by Django 4.1.6 on 2023-02-08 08:27

from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AchieveEvents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('description', models.TextField(default='')),
                ('result', models.TextField(default='Результаты будут позже')),
                ('image', models.ImageField(upload_to='', verbose_name='achieve/main/')),
                ('video', embed_video.fields.EmbedVideoField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'банк',
                'verbose_name_plural': 'банки',
            },
        ),
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('info', models.TextField(default='')),
            ],
            options={
                'verbose_name': 'тренер',
                'verbose_name_plural': 'тренеры',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254)),
                ('description', models.TextField(default='')),
                ('image', models.ImageField(upload_to='newsImage/main/')),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Новости',
                'verbose_name_plural': 'Новости',
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='Pol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'пол',
                'verbose_name_plural': 'пол',
            },
        ),
        migrations.CreateModel(
            name='Turnir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('address', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Предстоящие турниры',
                'verbose_name_plural': 'Предстоящие турнир',
            },
        ),
        migrations.CreateModel(
            name='WeightCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Весовые категории',
                'verbose_name_plural': 'Весовые категории',
            },
        ),
        migrations.CreateModel(
            name='Sportsmen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=253)),
                ('image', models.ImageField(upload_to='avatars/')),
                ('age', models.IntegerField()),
                ('fight', models.IntegerField()),
                ('weight', models.FloatField()),
                ('rating_total', models.FloatField()),
                ('pol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.pol')),
                ('weight_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.weightcategory')),
            ],
            options={
                'verbose_name': 'Спортсмены',
                'verbose_name_plural': 'Спортсмен',
            },
        ),
        migrations.CreateModel(
            name='NewsImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='newsImage/all/')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.news')),
            ],
            options={
                'verbose_name': 'Галерея новостей',
                'verbose_name_plural': 'Галерея новостей',
            },
        ),
        migrations.CreateModel(
            name='NewsAchieveEvents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='achieveImage/all/')),
                ('achieve', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.achieveevents')),
            ],
            options={
                'verbose_name': 'Галерея прошедшиъ турниров',
                'verbose_name_plural': 'Галерея прошедших турниров',
            },
        ),
        migrations.CreateModel(
            name='Donate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_account', models.CharField(max_length=255)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.bank')),
            ],
            options={
                'verbose_name': 'реквизит',
                'verbose_name_plural': 'реквизиты',
            },
        ),
    ]
