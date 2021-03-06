# Generated by Django 3.1.4 on 2021-06-26 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('addressaddr', models.CharField(db_column='addressAddr', max_length=25, primary_key=True, serialize=False)),
                ('officename', models.CharField(blank=True, db_column='officeName', max_length=20, null=True, unique=True)),
            ],
            options={
                'db_table': 'address',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('eventname', models.CharField(db_column='eventName', max_length=20, primary_key=True, serialize=False)),
                ('eventaddressaddr', models.CharField(db_column='eventAddressAddr', max_length=20)),
                ('eventphonenrtxt', models.CharField(db_column='eventPhoneNrTxt', max_length=20)),
                ('guestsnr', models.IntegerField(db_column='guestsNr')),
            ],
            options={
                'db_table': 'event',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Eventcode',
            fields=[
                ('eventcodenr', models.AutoField(db_column='eventCodeNr', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'eventcode',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Id',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'id',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Officer',
            fields=[
                ('officername', models.CharField(db_column='officerName', max_length=25, primary_key=True, serialize=False)),
                ('titlecode', models.CharField(db_column='titleCode', max_length=63)),
                ('agenr', models.IntegerField(blank=True, db_column='ageNr', null=True)),
                ('officename', models.CharField(blank=True, db_column='officeName', max_length=20, null=True)),
            ],
            options={
                'db_table': 'officer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Responsibilitydescription',
            fields=[
                ('responsibilitydescriptiontxt', models.CharField(db_column='responsibilityDescriptionTxt', max_length=500, primary_key=True, serialize=False)),
                ('titlecode', models.CharField(db_column='titleCode', max_length=63, unique=True)),
            ],
            options={
                'db_table': 'responsibilitydescription',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('volunteername', models.CharField(db_column='volunteerName', max_length=25, primary_key=True, serialize=False)),
                ('agenr', models.IntegerField(blank=True, db_column='ageNr', null=True)),
                ('officename', models.CharField(blank=True, db_column='officeName', max_length=20, null=True)),
                ('fname', models.CharField(db_column='fname', max_length=25)),
                ('mname', models.CharField(db_column='mname', max_length=25)),
                ('lname', models.CharField(db_column='lname', max_length=25)),
                ('gender', models.CharField(db_column='gender', max_length=25)),
                ('streetaddress', models.CharField(db_column='streetaddress', max_length=30)),
                ('city', models.CharField(db_column='city', max_length=25)),
                ('state', models.CharField(db_column='state', max_length=2)),
                ('zipcode', models.CharField(db_column='zipcode', max_length=5)),
                ('email', models.CharField(db_column='email', max_length=50)),
                ('phone', models.CharField(db_column='phone', max_length=12)),
                ('country', models.CharField(db_column='country', max_length=25)),
                ('dob', models.CharField(db_column='dob', max_length=20)),
                ('age', models.CharField(db_column='age', max_length=3)),
            ],
            options={
                'db_table': 'volunteer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Employmentdates',
            fields=[
                ('officename', models.CharField(db_column='officeName', max_length=25)),
                ('officername', models.OneToOneField(db_column='officerName', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='myapi.officer')),
                ('startdate', models.DateField(db_column='startDate')),
                ('enddate', models.DateField(db_column='endDate')),
            ],
            options={
                'db_table': 'employmentdates',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Eventdetails',
            fields=[
                ('eventname', models.OneToOneField(db_column='eventName', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='myapi.event')),
                ('volunteerreqdate', models.DateField(db_column='volunteerReqDate')),
                ('volunteerenddate', models.DateField(db_column='volunteerEndDate')),
            ],
            options={
                'db_table': 'eventdetails',
                'managed': False,
            },
        ),
    ]
