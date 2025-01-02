# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Users(models.Model):

    #__Users_FIELDS__
    firstname = models.TextField(max_length=255, null=True, blank=True)
    lastname = models.TextField(max_length=255, null=True, blank=True)
    empid = models.CharField(max_length=255, null=True, blank=True)
    userrole = models.ForeignKey(Roles, on_delete=models.CASCADE)
    isvalid = models.IntegerField(null=True, blank=True)

    #__Users_FIELDS__END

    class Meta:
        verbose_name        = _("Users")
        verbose_name_plural = _("Users")


class Roles(models.Model):

    #__Roles_FIELDS__
    rolename = models.TextField(max_length=255, null=True, blank=True)
    roletype = models.IntegerField(null=True, blank=True)

    #__Roles_FIELDS__END

    class Meta:
        verbose_name        = _("Roles")
        verbose_name_plural = _("Roles")


class Permissions(models.Model):

    #__Permissions_FIELDS__
    permissionname = models.TextField(max_length=255, null=True, blank=True)
    userrole = models.ForeignKey(Roles, on_delete=models.CASCADE)
    permissionvalues = models.IntegerField(null=True, blank=True)

    #__Permissions_FIELDS__END

    class Meta:
        verbose_name        = _("Permissions")
        verbose_name_plural = _("Permissions")


class Pages(models.Model):

    #__Pages_FIELDS__
    pagelink = models.TextField(max_length=255, null=True, blank=True)
    userrole = models.ForeignKey(Roles, on_delete=models.CASCADE)

    #__Pages_FIELDS__END

    class Meta:
        verbose_name        = _("Pages")
        verbose_name_plural = _("Pages")



#__MODELS__END
