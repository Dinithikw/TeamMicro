from django.shortcuts import render
from .models import Kyc_Info
from django.contrib import messages


def index(request):
    return render(request, 'kyc/index.html')


def personal(request):
    return render(request, 'kyc/(1st)PersonContact.html')


def account(request):
    return render(request, 'kyc/(2nd)AccEmp.html')


def office(request):
    return render(request, 'kyc/(4th)office.html')

def insertkyc(request):
    print("successfully completed")
    full_name = request.POST["fullname"]
    name_init = request.POST["nwi"]
    id_type = request.POST["ID_type"]
    nics_no = request.POST["NIC"]

    print(full_name)
    print(name_init)
    print(id_type)
    print(nics_no)

    submit_kyc = Kyc_Info()
    submit_kyc = Kyc_Info(full_name=full_name, name_init=name_init, id_type=id_type, nics_no=nics_no)
    submit_kyc.save()
    messages.success(request, 'Successfully submitted')

    return render(request, 'kyc/index.html')

    """if request.method=='POST':
        if request.POST.get('ID_type'):
            savekyc = Kyc_info()
            savekyc = request.POST.get('ID_type')
            savekyc.save()
            messages.success(request, 'successful')
            return render(request, 'kyc/index.html')

    else:
        return render(request, 'kyc/index.html')"""