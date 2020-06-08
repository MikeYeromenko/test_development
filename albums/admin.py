from django.contrib import admin


from albums.models import Album, Track


admin.site.register(Album)
admin.site.register(Track)
