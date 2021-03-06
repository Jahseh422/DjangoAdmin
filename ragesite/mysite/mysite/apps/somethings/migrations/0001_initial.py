# Generated by Django 4.0.5 on 2022-06-26 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Something',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('something_title', models.CharField(max_length=250, verbose_name='Список интерфейсов')),
                ('something_text', models.TextField(verbose_name='Именно список')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=50, verbose_name='Имя автора')),
                ('comment_text', models.CharField(max_length=200, verbose_name='Text')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='somethings.something')),
            ],
        ),
    ]
