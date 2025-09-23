from django.contrib import admin
from .models import Speaker, ProgramModule, Participant, SiteSettings

admin.site.register(Speaker)
admin.site.register(ProgramModule)
admin.site.register(Participant)
admin.site.register(SiteSettings)
