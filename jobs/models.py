from django.db import models


JOB_TYPES = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time')
)
# Create your models here.
class jobs (models.Model): #table
    title = models.CharField(max_length=100) #column
    #location
    job_type = models.CharField(max_length=30, choices=JOB_TYPES)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy=models.IntegerField(default=1)
    salary= models.IntegerField(default=0)
    experience=models.IntegerField(default=1)

    def __str__(self):
        return self.title
   