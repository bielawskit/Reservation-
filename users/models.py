from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin, Group
from django.db import models


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, name, surname, password=None):
        if not email:
            raise ValueError("Users must provide email")

        user = self.model(email=self.normalize_email(email), name=name, surname=surname)
        user.set_password(password)

        user.is_active = True
        user.save(using=self._db)

        if user.is_club:
            clubs_group = Group.objects.get(name="clubs")
            user.groups.add(clubs_group)
        else:
            players_group = Group.objects.get(name="players")
            user.groups.add(players_group)
        return user

    def create_superuser(self, email, name, surname, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            name=name,
            surname=surname,
            password=password,
        )

        user.is_active = True
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.is_club = True
        user.save(using=self._db)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name="Email", max_length=60, unique=True)
    name = models.CharField(max_length=25, verbose_name="Imię")
    surname = models.CharField(max_length=30, verbose_name="Nazwisko")
    is_club = models.BooleanField(default=False)
    date_join = models.DateTimeField(verbose_name="Date joined", auto_now_add=True)
    nip = models.CharField(max_length=20, blank=True, null=True)
    telephone_number = models.CharField(max_length=12, verbose_name="Numer telefonu")
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "surname"]

    objects = CustomUserManager()

    def __str__(self):
        return self.name
