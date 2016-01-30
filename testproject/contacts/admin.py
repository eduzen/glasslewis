from django.contrib import admin
from models import Company, Contact, Address, Email, Phone


class PhoneInLine(admin.TabularInline):
    model = Phone


class AddressInLine(admin.TabularInline):
    model = Address


class EmailInLine(admin.TabularInline):
    model = Email


class ContactAdmin(admin.ModelAdmin):
    inlines = [
        AddressInLine,
        PhoneInLine,
        EmailInLine
    ]

admin.site.register(Company)
admin.site.register(Contact, ContactAdmin)
