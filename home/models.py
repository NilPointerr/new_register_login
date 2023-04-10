from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
# Create your models here.
from django.db import models




from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager
from leave_clone import settings




class User(AbstractUser):

    department_choices=(
                        ('FINANCE','FINANCE'),
                        ('SALES','SALES'),
                        ('DEVELOPER','DEVELOPER'),
                        ('HR','HR'),
    )

    role_choices=(
                    ('BDE','BDE'),
                    ('EMPLOYEE','EMPLOYEE'),
                    ('HR','HR'),
                )
    
    employee_choices=(
                        ('FULL-TIME','FULL-TIME'),
                        ('PART-TIME','PART-TIME'),
                        ('INTERN','INTERN'),

                     )

    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    username=models.CharField(max_length=30,unique=True)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=5000)
    image=models.ImageField(upload_to='images/',default=None)
    birth_date=models.DateField(null=True)
    employee_joining_date=models.DateField(null=True)
    department=models.CharField(max_length=100,choices=department_choices)
    role=models.CharField(max_length=100,choices=role_choices)
    employee_type=models.CharField(max_length=100,choices=employee_choices)

    object = UserManager()


    USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS =[]

    def full_name(self):
        return self.first_name + "" + self.last_name







