# Generated by Django 3.1.7 on 2021-04-08 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Id_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nic_no', models.CharField(max_length=50)),
                ('name_full', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Kyc_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('name_init', models.CharField(max_length=100)),
                ('id_type', models.CharField(max_length=50)),
                ('nics_no', models.CharField(max_length=50)),
                ('driv_lic', models.CharField(max_length=50)),
                ('driv_exp', models.CharField(max_length=20)),
                ('pass_no', models.CharField(max_length=50)),
                ('pass_exp', models.CharField(max_length=20)),
                ('nationality', models.CharField(max_length=50)),
                ('nationality_other', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField(verbose_name='%Y-%m-%d')),
                ('house_no', models.CharField(max_length=20)),
                ('street', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('mob_no', models.CharField(max_length=20)),
                ('office_num', models.CharField(max_length=20)),
                ('home_num', models.CharField(max_length=20)),
                ('email_add', models.CharField(max_length=50)),
                ('occu_state', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Kyc_Infotemp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name_temp', models.CharField(max_length=200)),
                ('name_init_temp', models.CharField(max_length=100)),
                ('nics_no_temp', models.CharField(max_length=50)),
                ('driv_lic_temp', models.CharField(max_length=50)),
                ('driv_exp_temp', models.CharField(max_length=20)),
                ('pass_no_temp', models.CharField(max_length=50)),
                ('pass_exp_temp', models.CharField(max_length=20)),
                ('nationality_temp', models.CharField(max_length=50)),
                ('nationality_other_temp', models.CharField(max_length=50)),
                ('date_of_birth_temp', models.DateField(verbose_name='%Y-%m-%d')),
                ('house_no_temp', models.CharField(max_length=20)),
                ('street_temp', models.CharField(max_length=20)),
                ('city_temp', models.CharField(max_length=20)),
                ('country_temp', models.CharField(max_length=20)),
                ('mob_no_temp', models.CharField(max_length=20)),
                ('office_num_temp', models.CharField(max_length=20)),
                ('home_num_temp', models.CharField(max_length=20)),
                ('email_add_temp', models.CharField(max_length=50)),
                ('occu_state_temp', models.CharField(max_length=50)),
            ],
        ),
    ]
