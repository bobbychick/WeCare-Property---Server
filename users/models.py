from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)
from uuid import uuid4

# Create your models here.
class CustomUserModelManager(BaseUserManager):

    # objects = UserManager()

    def create_user(self, username, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not username:
            raise ValueError("Users must have a username")

        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            username=username,
            email=email,
            password=password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.admin = True
        user.save(using=self._db)
        return user


# User class which will encompass all users
class CustomUserModel(AbstractBaseUser, PermissionsMixin):

    ### Users will be grouped into the following three roles which have varying
    ### levels of permissions
    # 1. Owner =  Owner of the business - will have full set of permissions
    # relating to their business account and can create admins and other users
    # 2. Admin = Admin of the business - will have permissions such as: CRUD users
    # 3. User = Base user which will have core permissions such as view permissions

    # Fields that our users will have,
    userId = models.CharField(
        max_length=50, default=uuid4, primary_key=True, editable=True
    )

    username = models.CharField(max_length=20, unique=True, null=False, default=False)
    email = models.EmailField(max_length=100, unique=True, null=False, blank=False)

    # All users should be staff, however system managers and IT support are not staff
    # hence the option
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    # Password field is built into the AbstractBaseUser super class.
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]  #  Password is required by default.

    objects = CustomUserModelManager()

    class Meta:
        verbose_name = "Custom User"
