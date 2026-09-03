from django.contrib import admin
from .models import Leadt, Agent, User

# Register your models here.
admin.site.register(Leadt)
admin.site.register(Agent)
admin.site.register(User)