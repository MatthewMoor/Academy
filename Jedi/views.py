from django.shortcuts import render
from Jedi.models import Candidate, Jedi

# Create your views here.
def index(request):
    """View function for home page of site."""
    num_candidates = Candidate.objects.all().count()
    num_jedi = Jedi.objects.all().count()

    context = {
        'num_candidates': num_candidates,
        'num_jedi': num_jedi,
    }

    return render(request, 'index.html', context=context)