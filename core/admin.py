from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Transaction)
# admin.site.register(UserList)
admin.site.register(Bucket)
admin.site.register(WatchList)
admin.site.register(Stock)
admin.site.register(Multiplier)
