# Generated by Django 2.2 on 2019-04-24 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='sended', max_length=255)),
                ('text', models.TextField(default='no_text')),
                ('reciever', models.CharField(default='anon', max_length=255)),
                ('additional', models.CharField(default='no email', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(default='anon', max_length=255)),
                ('password', models.CharField(default='password', max_length=255)),
            ],
        ),
    ]
