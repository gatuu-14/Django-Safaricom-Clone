
from django.contrib import admin
from .models import UserProfile,Payment,Transaction
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Payment)
admin.site.register(Transaction)