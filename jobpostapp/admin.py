from django.contrib import admin
from jobpostapp.models import jobpost,job,post

# Register your models here.
admin.site.register(jobpost)
admin.site.register(job)
admin.site.register(post)