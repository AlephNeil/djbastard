from django.db import models
from django.utils import timezone
import re
from django.contrib.auth.models import User

# Create your models here.

class Enquiry(models.Model):
    STATUSES = (
        ('New', 'New enquiry not yet seen'),
        ('Handling', 'In contact with client, not yet quoted'),
        ('Quoted', 'Quote sent to client, awaiting response'),
        ('Closed - Accepted', 'Client accepted quote'),
        ('Closed - Not Accepted', 'Client refused or did not reply'),
        ('Closed - Not Quoted', 'We could not help client'),
    )
    caller_name = models.CharField('Caller\'s name', max_length=100)
    phone_number = models.CharField('Caller\'s phone number', max_length=20)
    details = models.CharField('Details of enquiry', max_length=255)
    who_for = models.ForeignKey(User, on_delete=models.CASCADE)

    response = models.CharField('Action taken', max_length=255, null=True, blank=True)
    date_quoted = models.DateTimeField('Date quote was sent')
    remarks = models.CharField('General remarks', max_length=255, null=True, blank=True)

    status = models.CharField('Status of enquiry', max_length=30, choices=STATUSES)

    created = models.DateTimeField('Date enquiry created', auto_now_add=True)
    updated = models.DateTimeField('Date of last update', auto_now=True)

    def is_open(self):
        return re.match(r'^Closed', self.status, re.I) is None

    def css_class(self):
        if self.status == 'New':
            return 'info'
        elif self.is_open():
            return 'active'
        elif self.status == 'Closed - Accepted':
            return 'success'
        else:
            return 'danger'