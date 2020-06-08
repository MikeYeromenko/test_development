from django.contrib import admin


from solos.models import Solo


class SoloAdmin(admin.ModelAdmin):
    model = Solo
    list_display = ['track', 'artist', 'get_duration']

    # def get_duration(self):
    #     return self.model.get_duration()


admin.site.register(Solo, SoloAdmin)

