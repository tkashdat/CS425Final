# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Address(models.Model):
    st_address = models.CharField(unique=True)
    city = models.CharField()
    state = models.CharField(max_length=2)
    zipcode = models.CharField()
    addressid = models.IntegerField(primary_key=True)
    officeid = models.ForeignKey('RealEstateOffice', models.DO_NOTHING, db_column='officeid')
    propertyid = models.ForeignKey('Property', models.DO_NOTHING, db_column='propertyid')

    class Meta:
        managed = False
        db_table = 'address'
        verbose_name_plural = 'addresses'


class Discount(models.Model):
    discount_amt = models.DecimalField(max_digits=4, decimal_places=2)
    discountid = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'discount'
        verbose_name_plural = 'discounts'


class Has(models.Model):
    renterid = models.OneToOneField('Renter', models.DO_NOTHING, db_column='renterid')
    paymentid = models.ForeignKey('Payments', models.DO_NOTHING, db_column='paymentid')

    class Meta:
        managed = False
        db_table = 'has'
        unique_together = (('renterid', 'paymentid'),)
        verbose_name_plural = 'hases'

    renterid = models.IntegerField()
    paymentid = models.IntegerField()


class Neighborhood(models.Model):
    walkability_score = models.IntegerField()
    crime_rate = models.DecimalField(max_digits=4, decimal_places=2)
    school_rating = models.CharField(max_length=1)
    neighborhoodid = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'neighborhood'
        verbose_name_plural = 'neighborhoods'


class Payments(models.Model):
    pmt_type = models.CharField()
    card_num = models.IntegerField(unique=True)
    expiration = models.CharField()
    ccv = models.IntegerField()
    paymentid = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'payments'
        verbose_name_plural = 'payments'


class Property(models.Model):
    sq_ft = models.IntegerField()
    no_bedrooms = models.IntegerField()
    no_baths = models.IntegerField()
    pool = models.CharField(max_length=1)
    property_type = models.CharField()
    description = models.CharField()
    monthly_rent = models.DecimalField(max_digits=10, decimal_places=2)
    rent_start_date = models.DateField()
    rent_end_date = models.DateField()
    propertyid = models.IntegerField(primary_key=True)
    discountid = models.ForeignKey(Discount, models.DO_NOTHING, db_column='discountid')
    neighborhoodid = models.ForeignKey(Neighborhood, models.DO_NOTHING, db_column='neighborhoodid')
    realtorid = models.ForeignKey('Realtor', models.DO_NOTHING, db_column='realtorid')

    class Meta:
        managed = False
        db_table = 'property'
        verbose_name_plural = 'properties'


class RealEstateOffice(models.Model):
    office_ph_num = models.CharField()
    officeid = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'real_estate_office'
        verbose_name_plural = 'real_estate_offices'


class Realtor(models.Model):
    commission = models.DecimalField(max_digits=4, decimal_places=2)
    realtorid = models.IntegerField(primary_key=True)
    officeid = models.ForeignKey(RealEstateOffice, models.DO_NOTHING, db_column='officeid')

    class Meta:
        managed = False
        db_table = 'realtor'
        verbose_name_plural = 'realtors'


class Renter(models.Model):
    primary_pmt = models.IntegerField()
    secondary_pmt = models.IntegerField()
    ssn = models.IntegerField(unique=True)
    renterid = models.IntegerField(primary_key=True)
    rewards = models.ForeignKey('Rewards', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'renter'
        verbose_name_plural = 'renters'


class Rents(models.Model):
    renterid = models.OneToOneField(Renter, models.DO_NOTHING, db_column='renterid')
    propertyid = models.ForeignKey(Property, models.DO_NOTHING, db_column='propertyid')

    class Meta:
        managed = False
        db_table = 'rents'
        unique_together = (('renterid', 'propertyid'),)
        verbose_name_plural = 'rents'

    renterid = models.IntegerField()
    paymentid = models.IntegerField()


class Rewards(models.Model):
    points_balance = models.IntegerField()
    rewards_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'rewards'
        verbose_name_plural = 'rewards'


class Transactions(models.Model):
    total = models.DecimalField(max_digits=10, decimal_places=2)
    discount_amt = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    approv_code = models.CharField(unique=True)
    pmt_amt = models.DecimalField(max_digits=10, decimal_places=2)
    transactionid = models.IntegerField(primary_key=True)
    paymentid = models.ForeignKey(Payments, models.DO_NOTHING, db_column='paymentid')
    discountid = models.ForeignKey(Discount, models.DO_NOTHING, db_column='discountid')
    propertyid = models.ForeignKey(Property, models.DO_NOTHING, db_column='propertyid')

    class Meta:
        managed = False
        db_table = 'transactions'
        verbose_name_plural = 'transactions'


class Users(models.Model):
    fname = models.CharField()
    lname = models.CharField()
    role = models.CharField(max_length=3)
    ph_number = models.CharField()
    user_id = models.IntegerField(primary_key=True)
    renterid = models.ForeignKey(Renter, models.DO_NOTHING, db_column='renterid')
    addressid = models.ForeignKey(Address, models.DO_NOTHING, db_column='addressid')
    realtorid = models.ForeignKey(Realtor, models.DO_NOTHING, db_column='realtorid')

    class Meta:
        managed = False
        db_table = 'users'
        verbose_name_plural = 'users'
