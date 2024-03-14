from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models



class UserManager(BaseUserManager):
    def create_user(self, email,  phone_number, password=None, **extra_fields):
        if not email and not phone_number:
            raise ValueError('Users must have an email address or phone number')
        if email:
            email = self.normalize_email(email)
        user = self.model(email=email, phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone_number,password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, phone_number, password, **extra_fields)
