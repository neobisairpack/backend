import jwt

from django.db import models
from django.conf import settings
from django.db.models import Avg
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from datetime import datetime, timedelta


class MyUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise TypeError("Please, enter your email.")

        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(
            username=username,
            email=email,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    USER_GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    )
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    username = models.CharField(max_length=64, unique=True)
    email = models.EmailField(unique=True)
    birthday = models.DateField(null=True)
    gender = models.CharField(max_length=16, choices=USER_GENDER)
    phone = models.CharField(max_length=64, unique=True)
    country = models.CharField(max_length=128)
    zip_code = models.CharField(max_length=32)
    state = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    image = models.ImageField(null=True, blank=True)
    points = models.IntegerField(default=20)
    rate = models.FloatField(default=0.0)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    objects = MyUserManager()

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    @property
    def token(self):
        return self._generate_jwt_token()

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=60)
        token = jwt.encode({
            'id': self.pk,
            'exp': dt.utcfromtimestamp(dt.timestamp())
        }, settings.SECRET_KEY, algorithm='HS256')
        return token.decode('utf-8')


class Rating(models.Model):
    requester = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='give_rate')
    provider = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='receive_rate')
    rating = models.FloatField(validators=(MinValueValidator(1.0), MaxValueValidator(5.0)))
    text = models.TextField(max_length=512)
    date = models.DateField(auto_now_add=True)


class AvgRating(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    avg_rating = models.FloatField()


@receiver(post_save, sender=Rating)
def save_user_rating(sender, instance, created, **kwargs):
    avg_rating, created = AvgRating.objects.get_or_create()
    if avg_rating.user.username == instance.provider.username:
        avg_rating.avg_rating = instance.rating
        avg_rating.save()

