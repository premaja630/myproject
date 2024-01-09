from django.shortcuts import render
from jobpostapp.models import jobpost,job
from django.views.generic import ListView,DetailView,CreateView

# Create your views here.
def job(request):
    pavan=jobpost.objects.all()
    return render(request,"jobpost/jobpost.html",{'pavan':pavan})
class detail_view(DetailView):
    context_object_name = 'details'
    model = jobpost