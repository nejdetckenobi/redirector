from django.shortcuts import redirect
from redirections.service import RedirectionService
from django.http import Http404


def forward(request, unique_id):
    service = RedirectionService()
    redirection = service.get_by_unique_id(unique_id)
    if redirection is None:
        raise Http404()

    forward_url = redirection.url
    return redirect(forward_url, permanent=redirection.is_permanent)
