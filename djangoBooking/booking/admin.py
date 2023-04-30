from django.contrib import admin
from .models import *

# Register your models here.
class AddressAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": {"addressid"}}

class DiscountAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": {"discountid"}}

class HasAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": {"renterid", "paymentid"}}

class NeighborhoodAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": {"neighborhoodid"}}

class PaymentAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": {"paymentid"}}

class PropertyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": {"propertyid"}}

class RealEstateOfficeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": {"officeid"}}    

class RealtorAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": {"realtorid"}, "realtorid": {"user_id"}}   

class RenterAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": {"renterid"}, "renterid": {"user_id"}}   

class RentsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": {"renterid", "propertyid"}, "renterid": {"user_id"}}

class RewardsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": {"rewards_id"}}

class TransactionsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": {"transactionid"}}

class UsersAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": {"user_id"}}

admin.site.register(Address, AddressAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(Has, HasAdmin)
admin.site.register(Neighborhood, NeighborhoodAdmin)
admin.site.register(Payments, PaymentAdmin)
admin.site.register(Property, PropertyAdmin)
admin.site.register(RealEstateOffice, RealEstateOfficeAdmin)
admin.site.register(Realtor, RealtorAdmin)
admin.site.register(Renter, RenterAdmin)
admin.site.register(Rents, RentsAdmin)
admin.site.register(Rewards, RewardsAdmin)
admin.site.register(Transactions, TransactionsAdmin)
admin.site.register(Users, UsersAdmin)