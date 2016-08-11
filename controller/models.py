from django.db import models

class Project(models.Model):
    name = models.CharField(max_length = 30)
    location = models.FileField(upload_to = 'projects/', default = 'under_construction.html')
