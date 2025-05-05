from django.db import models

# Create your models here.
# from django.contrib.auth.models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    """ Manager for user profiles """
    def create_user(self , name , password =None):
        """ Create a new user profile """
        if not email:
            raise ValueError("User must have an email")
        email = self.normalize_email(email)
        user = self.model(email=email , name=name)

        user.set_password(password)
        user.model(using=self._db)

        return User

    def create_superuser(self , email , name, password):
        """ Create and Sava a new superuser with """
        user = self.create_user(email, name ,password)

        user.is_superuser =True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser , PermissionsMixin):
    """ Database model for user in the system """
    email =  models.EmailField(max_length=255 , unique=True)
    name = models.CharField(max_length=255)
    is_Active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = [ 'name' ]

    def get_full_name(self):
        """ Retrieve full name of user """
        return self.name

    def get_short_name(self):
        """ Retrive short name of user"""
        return self.name

    def __str__(self):
        """ Return string representation of our user """
        return self.email
