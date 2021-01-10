from django.db import models
from django.urls import reverse
from django.utils import timezone
from typing import Tuple
from user.models import User


class LoyaltyModel(models.Model):

    card_status = [
        (1, "Active"),
        (2, "Not activated"),
        (3, "Expired")
    ]
    class Meta:
        unique_together = ('serial', 'card_number')


    serial = models.CharField(max_length=4, blank=False, null=False) #AA CG
    card_number = models.PositiveIntegerField()
    start_time = models.DateField(auto_now_add=True, auto_now=False)
    expiried_time = models.DateField(auto_now_add=False, auto_now=False)
    last_usage = models.DateField(auto_now_add=False, auto_now=True)
    bonus_ammount = models.DecimalField(max_digits=7, decimal_places=2, default= 0)
    status  =   models.PositiveIntegerField(choices=card_status, default=2)
    def __str__(self):
        return self.serial +" " + str(self.card_number)

    def check_expiration_date(self) -> Tuple[bool, int]:
        current_time = timezone.localdate()
        expires = self.expiried_time
        day_delta = abs(expires - current_time).days
        if expires >= current_time:
            return True, day_delta

        self.status = 3
        self.save()
        return False, day_delta

    def get_absolute_url(self):
        return reverse("card_detail", args=[str(self.pk)])


class Order(models.Model):
    product = models.CharField(max_length=120)
    loyalty_card = models.ForeignKey(LoyaltyModel, on_delete=models.CASCADE, related_name="orders")
    price = models.DecimalField(max_digits=7, decimal_places=2)
    date = models.DateField(auto_now_add=True, auto_now=False)
