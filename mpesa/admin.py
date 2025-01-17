
from django.contrib import admin
from .models import * # aterik imports all models in my models.py 
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Payment)
admin.site.register(Transaction)