# Generated by Django 4.2.1 on 2023-05-21 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_chatsession_chatentry_chat_session'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatSession1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
