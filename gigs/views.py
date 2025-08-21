from django.shortcuts import render
from .models import Gig

def gigs_list(request):
    gigs = Gig.objects.order_by('-posted_at')[:50]
    return render(request, "gigs/list.html", {"gigs": gigs})

