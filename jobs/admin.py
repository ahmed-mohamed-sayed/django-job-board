from django.contrib import admin

# Register your models here.
from .models import jobs , Category , Apply

admin.site.register(jobs)
admin.site.register(Category)
admin.site.register(Apply)

