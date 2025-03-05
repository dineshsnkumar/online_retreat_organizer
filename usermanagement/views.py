from django.shortcuts import render
from django.http import HttpResponse
from .models import Retreat, Recording
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def user_dashboard(request):
    retreat_list = Retreat.objects.all()
    context = {
        'retreat_list' : retreat_list,
    }
    return render(request,'usermanagement/retreat.html', context )


@login_required(login_url='login')
def retreat_details(request, retreat_id):
    retreat_detail = Retreat.objects.get(pk=retreat_id)
    context = {
        'retreat_detail': retreat_detail,
    }
    return render(request,'usermanagement/retreat_detail.html', context )


def retreat_recordings(request, retreat_id):
    recordings = Recording.objects.get(pk=retreat_id)
    context = {
        'recordings': recordings,
        'retreat_id': retreat_id,
    }
    return render(request,'usermanagement/recordings.html', context )

