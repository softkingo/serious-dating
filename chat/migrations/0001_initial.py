# Generated by Django 3.2.6 on 2022-01-23 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emoji',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('emoji', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gifts',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('gift', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_first', models.IntegerField()),
                ('user_second', models.IntegerField()),
                ('status', models.BooleanField(default=True)),
                ('blocked_by_user', models.IntegerField(null=True)),
                ('unblock_by_user', models.IntegerField(null=True)),
                ('instant_msg_status', models.BooleanField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('match', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.matchings')),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.IntegerField()),
                ('receiver', models.IntegerField()),
                ('message', models.TextField(null=True)),
                ('image', models.ImageField(null=True, upload_to='profile/')),
                ('video', models.FileField(null=True, upload_to='chat_videos/')),
                ('voice', models.FileField(null=True, upload_to='chat_voices/')),
                ('svg', models.CharField(default=None, max_length=200, null=True)),
                ('seen', models.BooleanField(default=False)),
                ('call_type', models.IntegerField(null=True)),
                ('call_status', models.IntegerField(null=True)),
                ('ended_by', models.IntegerField(null=True)),
                ('address', models.CharField(max_length=255, null=True)),
                ('latitude', models.CharField(max_length=255, null=True)),
                ('longitude', models.CharField(max_length=255, null=True)),
                ('time', models.TimeField(null=True)),
                ('date', models.DateField(null=True)),
                ('deleted_by_user1', models.IntegerField(default=False)),
                ('deleted_by_user2', models.IntegerField(default=False)),
                ('delete_chat_by_user1', models.IntegerField(default=False)),
                ('delete_chat_by_user2', models.IntegerField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group', to='chat.groups')),
            ],
        ),
    ]
