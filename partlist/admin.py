from django.contrib import admin

# Register your models here.
from .models import Part, Transaction

admin.site.register(Part)
admin.site.register(Transaction)
