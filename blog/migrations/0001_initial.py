# Generated by Django 3.2.3 on 2021-06-08 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('blog_content', models.TextField()),
                ('image_content', models.ImageField(upload_to='static/photos/')),
                ('pub_date', models.DateTimeField()),
                ('author', models.CharField(max_length=200)),
            ],
        ),
    ]
