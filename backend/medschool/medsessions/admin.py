from django.contrib import admin
from .models import Location, Session, SessionSchedule


admin.site.register(Location)
admin.site.register(Session)
admin.site.register(SessionSchedule)
