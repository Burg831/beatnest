from django.http import HttpResponse

def home(request):
    return HttpResponse("""<h1>BeatNest is live 🎶</h1><p>Find the Beat. Land the 
Gig.</p>""")


