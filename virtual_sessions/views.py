from django.shortcuts import render
from .models import Session


def seminar_search_page(request):
    """
    A view to return all the seminars
    """

    semniars = Session.objects.all()

    context = {
        'semniars': semniars,
    }

    return render(request, 'seminars/seminars.html')
