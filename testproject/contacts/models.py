from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator
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
    email = models.EmailField(unique=True)
    avatar = models.ImageField(
        upload_to=get_image_path,
        blank=True,
        null=True
    )
    phone_number = models.CharField(
        max_length=70,
        blank=True
    )

    def __unicode__(self):
        return "%s - %s" % (self.first_name, self.last_name)

    class Meta:
        verbose_name = ("Contact")
        verbose_name_plural = ("Contacts")
        ordering = ("last_name", )
