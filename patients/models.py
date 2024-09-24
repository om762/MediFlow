from django.db import models


# Patient details model for registration
class Patient(models.Model):
    '''
    It stores patient details which help in tracking of patient and helps deciding there priority of appointment.
    '''
    first_name = models.CharField(max_length=40, blank=False)
    last_name = models.CharField(max_length=40, blank=True, null=True)
    age = models.DecimalField(max_digits=3, decimal_places=0)
    father_name = models.CharField(max_length=40, blank=True, null=True)

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=95, blank=True, null=True)
    emergency_contact_number = models.CharField(max_length=15, blank=True, null=True)
    emergency_relation = models.CharField(max_length=20, blank=True, null=True)

    # TODO: Clear and efficient patient problem categories (Discussion)
    category_choices = [
        ('emergency', 'Emergency'),
        ('urgent', 'Urgent'),
        ('non_urgent', 'Non-Urgent'),
        ('chronic', 'Chronic Condition Management'),
        ('preventive', 'Preventive Care'),
        ('specialist', 'Specialist Referral'),
        ('follow_up', 'Follow-Up'),
    ]
    category = models.CharField(max_length=20, choices=category_choices, blank=True, null=True)


    PATIENT_PROBLEM = [
        ('medi_surg', 'Medical/Surgical'),
        ('trauma', 'Trauma'),
        ('obstetrics_gynecology', 'Obstetrics/Gynecology'),
        ('pediatric', 'Pediatric'),
        ('geriatric', 'Geriatric'),
        ('mental_health', 'Psychiatry/Mental Health'),
        ('oncology', 'Oncology'),
        ('rehabilitation', 'Rehabilitation'),
        ('infection', 'Infection Disease'),
        ('chronic', 'Chronic Disease'),
        ('special_care', 'Special Care')
    ]
    problem = models.CharField(max_length=30, choices=PATIENT_PROBLEM)

    MARITAL_STATUSES = [
        ('S', 'Single'),
        ('M', 'Married'),
        ('D', 'Divorced'),
        ('W', 'Widowed')
    ]
    marital_status = models.CharField(max_length=1, choices=MARITAL_STATUSES, blank=True, null=True)
    taking_any_medicines = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.category})"

    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"
        ordering = ['-created_at']