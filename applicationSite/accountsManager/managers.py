import uuid
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    User model with the email address as unique identifier.
    """

    def create_superuser(self, email, password, **user_fields):
        user_fields.setdefault('is_staff', True)
        user_fields.setdefault('is_superuser', True)
        user_fields.setdefault('is_active', True)

        if user_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if user_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **user_fields)

    def create_user(self, email, password, **user_fields):
        if not email:
            raise ValueError(_('Email is required'))
        email = self.normalize_email(email)
        user = self.model(email=email, **user_fields)
        user.set_password(password)
        user.save()
        return user
