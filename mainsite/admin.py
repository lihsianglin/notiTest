from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(User)
admin.site.register(Song)
admin.site.register(Viewlist)
admin.site.register(Favorite)
admin.site.register(Follow)
admin.site.register(Lyrics)
admin.site.register(Comment)
admin.site.register(Rating)