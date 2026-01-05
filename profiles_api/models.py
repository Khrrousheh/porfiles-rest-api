from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserProfileManager(BaseUserManager):
    """manager for user profiles"""
    def create_user(self, email, name, password=None):
        """Create New user Profile"""
        if not email:
            raise ValueError("User must have email address")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self.db)

        return user
    
    def create_superuser(self, email, name, password):
        """create superuser profile"""
        if not email:
            raise ValueError("superuser must have email address")
        if not password:
            raise ValueError("superuser must have password")
        
        user = self.model(email=email, name=name, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self.db)
        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    Database model for users in the system
    """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """retrive full name of user"""
        return self.name
    
    def get_short_name(self):
        return self.name
    
    def __str__(self):
        return self.email