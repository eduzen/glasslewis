from __future__ import unicode_literals

from django.db import models
from django.core.validators import URLValidator


def get_image_path(instance, filename):
    return '/'.join(['contact', instance.last_name, filename])


class Company(models.Model):
    # Attributes - Mandatory
    name = models.CharField(
        max_length=100,
        verbose_name=("name"),
        help_text=("Name of the company")
    )
    address_line1 = models.CharField(
        ('Address 1'),
        max_length=100,
        blank=True
    )
    address_line2 = models.CharField(
        ('Address 2'),
        max_length=100,
        blank=True
    )
    phone_number = models.CharField(
        max_length=70,
        blank=True
    )
    homepage = models.TextField(
        validators=[URLValidator()]
    )

    class Meta:
        verbose_name = ("Company")
        verbose_name_plural = ("Companies")
        ordering = ("name", )

    def __unicode__(self):
        return "%s" % (self.name)


class Contact(models.Model):
    # Relations
    company = models.ForeignKey(
        Company,
        related_name="company",
    )

    # Attributes
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    avatar = models.ImageField(
        upload_to=get_image_path,
        blank=True,
        null=True
    )

    @property
    def addresses(self):
        address = Address.objects.filter(contact=self)
        if address.exists():
            return address

    @property
    def phone(self):
        phone = Phone.objects.values("phone_number").filter(
            contact=self,
            main=True
        )
        if phone.exists():
            return phone[0]

    @property
    def phones(self):
        phones = Phone.objects.values("phone_number", "main").filter(
            contact=self,
        )
        if phones.exists():
            return phones

    @property
    def email(self):
        email = Email.objects.values("email").filter(contact=self, main=True)
        if email.exists():
            return email[0]

    @property
    def emails(self):
        email = Email.objects.values("email", "main").filter(contact=self)
        if email.exists():
            return email

    def __unicode__(self):
        return "%s - %s" % (self.first_name, self.last_name)

    class Meta:
        verbose_name = ("Contact")
        verbose_name_plural = ("Contacts")
        ordering = ("last_name", )


class Address(models.Model):
    # Relations
    contact = models.ForeignKey(Contact)

    # Attributes
    address_type = models.CharField(
        max_length=10,
    )
    address = models.CharField(
        max_length=255,
    )
    city = models.CharField(
        max_length=255,
    )
    state = models.CharField(
        max_length=20,
    )
    postal_code = models.CharField(
        max_length=20,
    )
    main = models.BooleanField(default=False)

    class Meta:
        verbose_name = ("Address")
        verbose_name_plural = ("Addresses")


class Email(models.Model):
    # Relations
    contact = models.ForeignKey(Contact)

    # Attributes
    email = models.EmailField(unique=True)
    main = models.BooleanField(default=False)

    class Meta:
        verbose_name = ("Email")
        verbose_name_plural = ("Emails")


class Phone(models.Model):
    # Relations
    contact = models.ForeignKey(Contact)

    # Attributes
    phone_number = models.CharField(
        max_length=70,
        blank=True
    )
    main = models.BooleanField(default=False)

    class Meta:
        verbose_name = ("Phone")
        verbose_name_plural = ("Phones")
