from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=120, blank=False, null=True)
    email = models.EmailField()
    full_name = models.CharField(max_length=120, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def  __str__(self):
        return self.user_name