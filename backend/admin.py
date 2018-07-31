from django.contrib import admin

from .models import *

admin.site.register(Member)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Budget)
admin.site.register(Transaction)