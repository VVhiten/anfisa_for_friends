from django.shortcuts import render


def proposal(request):
    return render(request, 'contest/form.html')