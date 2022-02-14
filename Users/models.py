from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords
from Company.models import Company, DistributionCenter


# Create your models here.

class Employees (models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    Code_Employees = models.CharField(("Codigo de empleado"),max_length=50)
    Position = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    Phone = models.CharField(("Numero de telefono"),max_length=50, blank=True)
    Email = models.EmailField(("Correo electronico"),max_length=50, blank=True)
    Manager = models.CharField(max_length=100, blank=True)
    DistributionCenter = models.ForeignKey(DistributionCenter, on_delete=models.CASCADE)
    history = HistoricalRecords()

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        ordering = ('first_name',)
        verbose_name = 'Empleados'
        verbose_name_plural = 'Empleados'


"""
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, Username, password=None):
        if not Username:
            raise ValueError('missing email')
        user = self.model(Username=Username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, Username, password):
        #for this example, nothing special happens here
        return self.create_user(Username, password)

class CustomUser(AbstractBaseUser):
    email = models.EmailField(max_length=254, unique=True,db_index=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)    
    Username = models.CharField(max_length=50, unique=True)
    firs_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'Username'

    def get_short_name(self):
        return self.email
    def get_full_name(self):
        return self.email



class UserProfiles(models.Model):
    Username = models.CharField(User, max_length=100)
    Password = models.CharField(User, max_length=100)
    firs_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('user_detail', args=[str(self.id)])

    def get_full_name(self):
        return self.user.get_full_name()

    def get_short_name(self):
        return self.user.get_short_name()

    def get_email(self):
        return self.user.email

    def get_phone(self):
        return self.phone

    def get_address(self):
        return self.address

    def get_city(self):
        return self.city

    def get_state(self):
        return self.state

    def get_country(self):
        return self.country

    def get_zip(self):
        return self.zip

    class Meta:
        ordering = ('user',)
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        
    """