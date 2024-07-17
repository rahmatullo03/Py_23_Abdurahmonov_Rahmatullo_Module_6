# Login Password = python2003

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db.models import Model, DateTimeField, CharField, TextField, ForeignKey, CASCADE, FloatField, \
    IntegerField, SlugField
from django.utils.text import slugify


class BaseModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    slug = SlugField(unique=True)

    class Meta:
        abstract = True

    def save( self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        while self.__class__.objects.filter(slug=self.slug).exists():
            self.slug += '-1'
        super().save(force_insert,force_update,using,update_fields)


class Category(BaseModel):
    class Meta:
        verbose_name_plural = 'Categories'
    name = CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(BaseModel):
    name = CharField(max_length=60)
    image = CharField(max_length=100)
    description = TextField()
    price = FloatField()
    color = CharField(max_length=50)
    category = ForeignKey('apps.Category',on_delete=CASCADE,related_name='products',to_field='slug')
    quantity = IntegerField()

    def __str__(self):
        return self.name


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractUser):
    email = CharField(max_length=50,unique=True)
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    username = CharField(max_length=100,null=True)
    phone_number = CharField(max_length=100)
    mobile_number = CharField(max_length=100)
    age = CharField(max_length=100)









