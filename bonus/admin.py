from django.contrib import admin

# Register your models here.
from bonus.models import LoyaltyModel
# Register your models here.


@admin.register(LoyaltyModel)
class LoyaltyAdmin(admin.ModelAdmin):
    date_hierarchy = "last_usage"
    search_fields = [
        "serial",
        "card_number",
    ]
    list_display = [
        "id",
        "serial",
        "card_number",
    ]