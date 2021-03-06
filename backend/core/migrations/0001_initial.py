# Generated by Django 4.0.1 on 2022-01-31 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('description', models.TextField(max_length=255, verbose_name='Описание')),
                ('logo', models.ImageField(upload_to='logo/', verbose_name='Логотип')),
            ],
            options={
                'verbose_name': 'Разработчик',
                'verbose_name_plural': 'Разработчики',
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Имя')),
                ('description', models.TextField(max_length=2000, verbose_name='Описание')),
                ('release_date', models.DateField(verbose_name='Дата выхода')),
                ('site', models.CharField(max_length=100, verbose_name='Сайт')),
                ('trailer', models.FileField(blank=True, upload_to='video/')),
                ('url', models.SlugField(max_length=100, unique=True)),
                ('developer', models.ManyToManyField(related_name='game_developer', to='core.Developer', verbose_name='Разработчик')),
            ],
            options={
                'verbose_name': 'Игра',
                'verbose_name_plural': 'Игры',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('url', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
            ],
            options={
                'verbose_name': 'Игровая платформа',
                'verbose_name_plural': 'Игровые платформы',
            },
        ),
        migrations.CreateModel(
            name='RatingStar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveSmallIntegerField(default=0, verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'Звезда рейтинга',
                'verbose_name_plural': 'Звезды рейтинга',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('text', models.TextField(max_length=6000, verbose_name='Рецензия')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='core.game', verbose_name='Игра')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='core.review', verbose_name='Предыдущий_коммент')),
            ],
            options={
                'verbose_name': 'Рецензия',
                'verbose_name_plural': 'Рецензии',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=100, verbose_name='IP адрес')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.game', verbose_name='Игра')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ratingstar', verbose_name='Звезда')),
            ],
            options={
                'verbose_name': 'Рейтинг',
                'verbose_name_plural': 'Рейтинги',
            },
        ),
        migrations.CreateModel(
            name='GameScreenShots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Имя')),
                ('image', models.ImageField(upload_to='image/', verbose_name='Изображение')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.game', verbose_name='Игра')),
            ],
            options={
                'verbose_name': 'Скриншот',
                'verbose_name_plural': 'Скриншоты',
            },
        ),
        migrations.AddField(
            model_name='game',
            name='genre',
            field=models.ManyToManyField(related_name='game_genre', to='core.Genre', verbose_name='Жанр'),
        ),
        migrations.AddField(
            model_name='game',
            name='platform',
            field=models.ManyToManyField(related_name='game_platform', to='core.Platform', verbose_name='Платформа'),
        ),
        migrations.AddField(
            model_name='game',
            name='publisher',
            field=models.ManyToManyField(related_name='game_publisher', to='core.Developer', verbose_name='Издатель'),
        ),
    ]
