from django.shortcuts import render
from .models import Session


def seminar_search_page(request):
    """
    A view to return all the seminars
    """

    seminars = Session.objects.all()

    context = {
        'seminars': seminars,
    }

    return render(request, 'seminars/seminars.html', context)
