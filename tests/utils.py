import random
import string
from django.utils import timezone
import datetime
from bonus.models import LoyaltyModel


def expiration_date_generator():
    date_range = [30, 180 , 365]
    end_date = timezone.localdate() + datetime.timedelta(days=random.choice(date_range))
    return end_date

def card_number_generator():
    return random.randint(0, 999999)

def serial_generator(count=3):
    return ''.join([ random.choice(string.ascii_uppercase) for i in range(count) ])

def random_cards_generator():
    return dict(serial=serial_generator(),
                card_number=card_number_generator(),
                expiried_time=expiration_date_generator())

def product_generator():
    product_list =["nintendo", "switch", "laptop", "ssd", "kindle", "ps4", "airpods", "ipad", "tablet", "iphone", "alexa", "TV", "mircowave", "HDD"]
    return random.choice(product_list)

def price_generator():
    return float(random.randrange(100, 1000))/100


def orders_generator():
    return dict(product = product_generator(),
                loyalty_card= LoyaltyModel.objects.last(),
                price= price_generator()
                )
