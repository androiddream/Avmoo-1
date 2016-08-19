from django.contrib import admin
from .models import avmoo_api
from .models import teacher

admin.site.register(teacher)
admin.site.register(avmoo_api)
