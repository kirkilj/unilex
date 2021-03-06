from django.db import models
from django.contrib.auth.models import User

class Feedback(models.Model):
    url = models.CharField(max_length=255, blank=True, verbose_name='URL')
    message = models.TextField()
    browser = models.CharField(max_length=500)
    user = models.ForeignKey(User, null=True, blank=True)
    email = models.CharField(max_length=255, blank=True)
    ip = models.CharField(max_length=225, blank=True, verbose_name='IP') # Might be comma-separated list.
    awesome = models.BooleanField(default=False)
    ignore = models.BooleanField(default=False)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField()

    def __str__(self):
        return '#%s: From %s' % (self.id, self.email or 'anonymous')

    class Meta:
        db_table = 'feedback'
