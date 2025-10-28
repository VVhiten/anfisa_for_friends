from django.http import HttpRequest
from django.shortcuts import render

from .forms import ContestForm


def proposal(request: HttpRequest):
    form = ContestForm(request.GET or None)
    context = {'form': form}
    return render(request, 'contest/form.html', context)