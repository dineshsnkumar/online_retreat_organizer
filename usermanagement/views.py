from django.shortcuts import render
from django.http import HttpResponse
from .models import Retreat

# Create your views here.
def user_dashboard(request):
    retreat_list = Retreat.objects.all()
    context = {

    }
    return render(request,'usermanagement/retreat.html', context )

def get_all_retreats(request):
    return HttpResponse("User has five past retreats")