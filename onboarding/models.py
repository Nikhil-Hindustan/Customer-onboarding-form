from django.db import models
from django.contrib.auth.models import User


class CountryModel(models.Model):
    name = models.CharField(max_length=100)


class DocumentSetModel(models.Model):
    name = models.CharField(max_length=100)
    countries = models.ManyToManyField(CountryModel)
    has_backside = models.BooleanField(default=False)
    ocr_labels = models.TextField()  # JSON String


class CustomerModel(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]

    NATION_CHOICES = [
        ('I', 'INDIA'),
        ('C', 'CHINA'),
        ('U', 'USA')
    ]

    surname = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=1, choices=NATION_CHOICES)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


class CustomerDocumentModel(models.Model):
    customer = models.ForeignKey(CustomerModel, on_delete=models.CASCADE)
    attached_file = models.FileField(upload_to='customer_documents/')
    extracted_json = models.TextField()  # JSON String
    created_at = models.DateTimeField(auto_now_add=True)
