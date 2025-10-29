from django.shortcuts import render, redirect, get_object_or_404

from .forms import ContestForm
from .models import Contest


def proposal(request, pk=None):
    if pk is None:
        instance = None
    else:
        instance = get_object_or_404(Contest, pk=pk)
    form = ContestForm(request.POST or None, instance=instance)
    context = {'form': form}
    if form.is_valid():
        form.save()
    return render(request, 'contest/form.html', context)


def delete_proposal(request, pk):
    instance = get_object_or_404(Contest, pk=pk)
    if request.method == 'POST':
        instance.delete()
        return redirect('contest:list')
    form = ContestForm(instance=instance)
    context = {'form': form}
    return render(request, 'contest/form.html', context)


def proposal_list(request):
    contest_proposals = Contest.objects.order_by('id')
    context = {'contest_proposals': contest_proposals}
    return render(request, 'contest/contest_list.html', context)