from django.contrib import admin
from .models import Main         # Registering the app so that it appears in admin page

# Register your models here.

admin.site.register(Main)       # Step 2 in registering the app