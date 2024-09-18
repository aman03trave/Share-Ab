# Generated by Django 4.2.6 on 2023-11-07 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('request_create_date', models.DateField()),
                ('trip_date_time', models.DateTimeField()),
                ('desc', models.CharField(max_length=100)),
                ('no_passengers', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female')], default='MALE', max_length=6),
        ),
        migrations.AddField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(default='', upload_to='users/images'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.CreateModel(
            name='Requested_users_status',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=False)),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.request')),
                ('user', models.ManyToManyField(related_name='request_status', to='users.user')),
            ],
        ),
        migrations.AddField(
            model_name='request',
            name='request_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
        migrations.AddField(
            model_name='request',
            name='requested_users',
            field=models.ManyToManyField(related_name='request_received', to='users.user'),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.CharField(max_length=100)),
                ('message_date', models.DateField()),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to='users.user')),
                ('request_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.request')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to='users.user')),
            ],
        ),
    ]
