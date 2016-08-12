from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):

    author = models.ForeignKey('auth.User', on_delete = models.CASCADE )
    title = models.CharField(max_length = 70, blank = False)
    body = models.TextField(blank = False)
    publish_date = models.DateField(blank = True)
    created_date = models.DateField(auto_now_add = True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()
