from django.shortcuts import render
from .models import Kyc_Info
from django.contrib import messages




def index(request):
    return render(request, 'kyc/index.html')

def account(request):
    return render(request, 'kyc/(2nd)AccEmp.html')

def personal(request):
    return render(request, 'kyc/(3rd)Declaration.html')


def office(request):
    return render(request, 'kyc/(4th)office.html')

def insertkyc1(request):
    global occu_state
    occu_state = request.POST["Occutation_Status"]
    print(occu_state)
    print(full_name)
    print(name_init)


    return render(request, 'kyc/(2nd)AccEmp.html')




def insertkyc(request):
    print("successfully completed")

    global full_name
    global name_init
    global id_type
    global nics_no
    full_name = request.POST["fullname"]
    name_init = request.POST["nwi"]
    id_type = request.POST["ID_type"]
    nics_no = request.POST["NIC"]


    messages.success(request, 'Successfully saved')


    print(full_name)
    print(name_init)
    print(id_type)
    print(nics_no)

    submit_kyc = Kyc_Info()
    submit_kyc = Kyc_Info(full_name=full_name, name_init=name_init, id_type=id_type, nics_no=nics_no)
    submit_kyc.save()
    messages.success(request, 'Successfully submitted')

    return render(request, 'kyc/(2nd)AccEmp.html')

    """if request.method=='POST':
        if request.POST.get('ID_type'):
            savekyc = Kyc_info()
            savekyc = request.POST.get('ID_type')
            savekyc.save()
            messages.success(request, 'successful')
            return render(request, 'kyc/index.html')

    else:
        return render(request, 'kyc/index.html')"""