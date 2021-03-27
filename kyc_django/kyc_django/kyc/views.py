from django.shortcuts import render


def index(request):
    return render(request, 'kyc/index.html')


def personal(request):
    return render(request, 'kyc/(1st)PersonContact.html')


def account(request):
    return render(request, 'kyc/(2nd)AccEmp.html')


def office(request):
    return render(request, 'kyc/(4th)office.html')
