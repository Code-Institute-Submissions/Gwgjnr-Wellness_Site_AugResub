from django.shortcuts import render, get_object_or_404
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


def seminar_detail(request, session_id):
    """
    A view to details for selected seminar
    """

    seminar = get_object_or_404(Session, pk=session_id)

    context = {
        'seminar': seminar,
    }

    return render(request, 'seminars/seminar_detail.html', context)
