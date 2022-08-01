# Generated by Django 4.0.6 on 2022-08-01 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Wallet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField()),
                ('account_number', models.IntegerField()),
                ('account_name', models.CharField(max_length=15, null=True)),
                ('account_type', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='ID_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='gender',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='password',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='first_name',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_name',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phonenumber',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField()),
                ('Date_created', models.DateTimeField()),
                ('status', models.CharField(max_length=10, null=True)),
                ('pin', models.IntegerField()),
                ('currency', models.CharField(max_length=10, null=True)),
                ('Customer', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='Wallet.customer')),
            ],
        ),
    ]