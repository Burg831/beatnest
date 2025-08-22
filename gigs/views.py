from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Gig

def gig_list(request):
    q = request.GET.get('q', '').strip()

    qs = Gig.objects.order_by('-posted_at')
    if q:
        qs = qs.filter(
            Q(title__icontains=q) |
            Q(company__icontains=q) |
            Q(location__icontains=q)
        )

    
    paginator = Paginator(qs, 10)
    page_obj = paginator.get_page(request.GET.get('page'))

    return render(request, 'gigs/list.html', {
        'q': q,
        'gigs': page_obj,      
        'page_obj': page_obj,  
    })

def gig_detail(request, pk):
    gig = get_object_or_404(Gig, pk=pk)
    return render(request, 'gigs/detail.html', {'gig': gig})

