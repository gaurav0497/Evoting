from django.contrib import admin

# Register your models here.
from .models import Candidate,Voter,Official
admin.site.register(Candidate)
admin.site.register(Voter)
admin.site.register(Official)