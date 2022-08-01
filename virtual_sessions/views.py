from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import View
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect
from .models import Session, Comment
from .forms import CommentForm


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
                messages.error(request, "Please enter a search query")
                return redirect(reverse('seminars'))

            queries = Q(title__icontains=query) | Q(summary__icontains=query) | Q(details__icontains=query)
            seminars = seminars.filter(queries)

    context = {
        'seminars': seminars,
        'search_term': query,
    }

    return render(request, 'seminars/seminars.html', context)


def seminar_detail(request, slug):
    """
    A view to details for selected seminar
    """

    seminar = get_object_or_404(Session, slug=slug)
    comments = seminar.comments.filter(approved=True, reply__isnull=True)

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Reply code to be added here
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.session = seminar
            comment.save()
            return HttpResponseRedirect(request.path_info)
    else:
        comment_form = CommentForm()

    context = {
        'seminar': seminar,
        'comments': comments,
        'comment_form': comment_form
    }

    return render(request, 'seminars/seminar_detail.html', context)


class JoinSeminar(View):
    '''
    A view for joining or cancelling your spot at a seminar.
    '''
    def post(self, request, title, *args, **kwargs):
        seminar = get_object_or_404(Session, title=title)
        next = request.POST.get('next', '/')
        if request.user in seminar.signed_up.all():
            seminar.signed_up.remove(request.user)
            messages.warning(request, f'You cancelled your place at {seminar.title}')
            seminar.save()

        else:
            seminar.signed_up.add(request.user)
            seminar.save()
            messages.success(request, f'You signed up for {seminar.title}')
        return HttpResponseRedirect(next)


class DeleteSeminar(View):
    '''
    A view for deleting a seminar.
    '''
    def post(self, request, title, *args, **kwargs):
        seminar = get_object_or_404(Session, title=title)
        seminar.delete()
        messages.info(request, f'You have deleted {seminar.title}')
        return redirect(reverse('seminars'))
