from django.shortcuts import render

from .forms import ContestForm
from .models import Contest


def proposal(request):
    # Допишите функцию, чтобы она могла работать как на создание заявки,
    # так и на редактирование.
    form = ContestForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        form.save()
    return render(request, 'contest/form.html', context)


def delete_proposal(request):
    # Допишите функцию для удаления заявок.
    return


def proposal_list(request):
    contest_proposals = Contest.objects.order_by('id')
    context = {'contest_proposals': contest_proposals}
    return render(request, 'contest/contest_list.html', context)