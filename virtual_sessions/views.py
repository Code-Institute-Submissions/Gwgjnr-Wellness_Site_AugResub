from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Session


def seminar_search_page(request):
    """
    A view to return all the seminars
    """

    seminars = Session.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter a search query!")
                return redirect(reverse('seminars'))

            queries = Q(title__icontains=query) | Q(summary__icontains=query) | Q(details__icontains=query)
            seminars = seminars.filter(queries)

    context = {
        'seminars': seminars,
        'search_term': query,
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
