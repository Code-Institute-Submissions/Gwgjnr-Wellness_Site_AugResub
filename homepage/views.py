from django.shortcuts import render
from virtual_sessions.models import Session


def index(request):
    """
    A view to return the homepage
    """
    seminars = Session.objects.all()

    context = {
        'seminars': seminars,
    }

    return render(request, 'homepage/index.html', context)
