# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Address(models.Model):
    addressaddr = models.CharField(db_column='addressAddr', primary_key=True, max_length=25)  # Field name made lowercase.
    officename = models.CharField(db_column='officeName', unique=True, max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'address'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Employmentdates(models.Model):
    officename = models.CharField(db_column='officeName', max_length=25)  # Field name made lowercase.
    officername = models.OneToOneField('Officer', models.DO_NOTHING, db_column='officerName', primary_key=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='startDate')  # Field name made lowercase.
    enddate = models.DateField(db_column='endDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employmentdates'
        unique_together = (('officername', 'startdate', 'officename'),)


class Event(models.Model):
    eventname = models.CharField(db_column='eventName', primary_key=True, max_length=20)  # Field name made lowercase.
    eventaddressaddr = models.CharField(db_column='eventAddressAddr', max_length=20)  # Field name made lowercase.
    eventcodenr = models.OneToOneField('Eventcode', models.DO_NOTHING, db_column='eventCodeNr')  # Field name made lowercase.
    eventphonenrtxt = models.CharField(db_column='eventPhoneNrTxt', max_length=20)  # Field name made lowercase.
    guestsnr = models.IntegerField(db_column='guestsNr')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'event'


class Eventcode(models.Model):
    eventcodenr = models.AutoField(db_column='eventCodeNr', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eventcode'


class Eventdetails(models.Model):
    eventname = models.OneToOneField(Event, models.DO_NOTHING, db_column='eventName', primary_key=True)  # Field name made lowercase.
    volunteername = models.ForeignKey('Volunteer', models.DO_NOTHING, db_column='volunteerName')  # Field name made lowercase.
    volunteerreqdate = models.DateField(db_column='volunteerReqDate')  # Field name made lowercase.
    volunteerenddate = models.DateField(db_column='volunteerEndDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eventdetails'
        unique_together = (('eventname', 'volunteername', 'volunteerreqdate'),)


class Id(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'id'


class Officer(models.Model):
    officername = models.CharField(db_column='officerName', primary_key=True, max_length=25)  # Field name made lowercase.
    eventname = models.ForeignKey(Event, models.DO_NOTHING, db_column='eventName')  # Field name made lowercase.
    titlecode = models.CharField(db_column='titleCode', max_length=63)  # Field name made lowercase.
    id = models.OneToOneField(Id, models.DO_NOTHING, db_column='ID', blank=True, null=True)  # Field name made lowercase.
    addressaddr = models.ForeignKey(Address, models.DO_NOTHING, db_column='addressAddr', blank=True, null=True)  # Field name made lowercase.
    agenr = models.IntegerField(db_column='ageNr', blank=True, null=True)  # Field name made lowercase.
    officename = models.CharField(db_column='officeName', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'officer'


class Responsibilitydescription(models.Model):
    responsibilitydescriptiontxt = models.CharField(db_column='responsibilityDescriptionTxt', primary_key=True, max_length=500)  # Field name made lowercase.
    titlecode = models.CharField(db_column='titleCode', unique=True, max_length=63)  # Field name made lowercase.
    volunteername = models.OneToOneField('Volunteer', models.DO_NOTHING, db_column='volunteerName')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'responsibilitydescription'


class Volunteer(models.Model):
    volunteername = models.CharField(db_column='volunteerName', primary_key=True, max_length=25)  # Field name made lowercase.
    addressaddr = models.ForeignKey(Address, models.DO_NOTHING, db_column='addressAddr', blank=True, null=True)  # Field name made lowercase.
    agenr = models.IntegerField(db_column='ageNr', blank=True, null=True)  # Field name made lowercase.
    officename = models.CharField(db_column='officeName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fname = models.CharField(db_column='fname', max_length=25)  # Field name made lowercase.
    mname = models.CharField(db_column='mname', max_length=25)  # Field name made lowercase.
    lname = models.CharField(db_column='lname', max_length=25)  # Field name made lowercase.
    gender = models.CharField(db_column='gender', max_length=25)  # Field name made lowercase.
    streetaddress = models.CharField(db_column='streetaddress', max_length=30)  # Field name made lowercase.
    city = models.CharField(db_column='city', max_length=25)  # Field name made lowercase.
    state = models.CharField(db_column='state', max_length=2)  # Field name made lowercase.
    zipcode = models.CharField(db_column='zipcode', max_length=5)  # Field name made lowercase.
    email = models.CharField(db_column='email', max_length=50)  # Field name made lowercase.
    phone = models.CharField(db_column='phone', max_length=12)  # Field name made lowercase.
    country = models.CharField(db_column='country', max_length=25)  # Field name made lowercase.
    dob = models.CharField(db_column='dob', max_length=20)  # Field name made lowercase.
    age = models.CharField(db_column='age', max_length=3)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'volunteer'