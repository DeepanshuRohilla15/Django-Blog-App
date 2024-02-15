from django.contrib import admin
from .models import Profile

#The admin.py file is used to display your models in the Django admin panel.
# You can also customize your admin panel.
admin.site.register(Profile)
