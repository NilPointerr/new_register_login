from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
# Create your models here.
from django.db import models

SICK = 'sick'
CASUAL = 'casual'
EMERGENCY = 'emergency'
STUDY = 'study'
MATERNITY = 'maternity'
BEREAVEMENT = 'bereavement'
QUARANTINE = 'quarantine'
COMPENSATORY = 'compensatory'
SABBATICAL = 'sabbatical'



class Leave_form(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,primary_key=True)
    typeofleave = [
        (SICK,'Sick Leave'),
        (CASUAL,'Casual Leave'),
        (EMERGENCY,'Emergency Leave'),
        (STUDY,'Study Leave'),
        (MATERNITY, 'Maternity Leave'),
        (BEREAVEMENT, 'Bereavement Leave'),
        (QUARANTINE, 'Self Quarantine'),
        (COMPENSATORY, 'Compensatory Leave'),
        (SABBATICAL, 'Sabbatical Leave')
    ]
    leaveday = [
        ('Full day', 'Full Day'),
        ('Half Day', 'Half Day'),
    ]
    statustype = [
        ('Pending','Pending'),
        ('Approved','Approved'),
        ('Cancel','Cancel'),
        ('Rejected','Rejected'),

    ]
    start_date = models.DateField()
    end_date = models.DateField()
    leave_type = models.CharField(max_length=100, choices=typeofleave)
    sub_leave = models.CharField(max_length=100, choices=leaveday)
    status = models.CharField(max_length=100,choices=statustype,default='Pending')

    # class Meta:
    #     managed = True
    #     db_table = 'leavein'
    