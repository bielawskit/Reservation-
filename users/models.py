from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin, Group
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, surname, password=None):
        if not email:
            raise ValueError('Users must provide email')

        user = self.model(email=self.normalize_email(email), name=name, surname=surname)
        user.set_password(password)

        user.is_active = True

        user.save(using=self._db)
        # if user.is_club:
        #     group = Group.objects.get(name='clubs')
        # else:
        #     group = Group.objects.get(name='players')
        # user.groups.add(group)
        return user

    def create_superuser(self, email, name, surname, password=None):
        user = self.create_user(email=self.normalize_email(email), name=name, surname=surname, password=password)

        user.is_active = True
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='User email', max_length=60, unique=True)
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=30)
    date_join = models.DateTimeField(verbose_name='Date joined', auto_now_add=True)
    NIP = models.CharField(max_length=20, unique=True, null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_club = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'surname']

    objects = CustomUserManager()

    def __str__(self):
        return self.name
