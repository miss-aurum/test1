# Generated by Django 4.1.6 on 2023-02-08 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Катигории')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('discription', models.TextField(verbose_name='Описание')),
                ('pub_date', models.DateTimeField(verbose_name='Дата публикации')),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alisher.categories')),
            ],
        ),
    ]
