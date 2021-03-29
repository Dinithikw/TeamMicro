from django.shortcuts import render
from .models import Kyc_Info
from django.contrib import messages


# define method for calling pages
# -----------------------------------------------------------------------------------------------------------------------

def index(request):
    return render(request, 'kyc/index.html')


def account(request):
    return render(request, 'kyc/(2nd)AccEmp.html')


def personal(request):
    return render(request, 'kyc/(3rd)Declaration.html')


def office(request):
    return render(request, 'kyc/(4th)office.html')


# -----------------------------------------------------------------------------------------------------------------------

# defining method to call accounts page and applying values to the variables
def insertkyc1(request):
    global occu_state
    occu_state = request.POST["Occutation_Status"]
    print(occu_state)
    print(full_name)
    print(name_init)

    submit_kyc = Kyc_Info(full_name=full_name, name_init=name_init, id_type=id_type, nics_no=nics_no,
                          occu_state=occu_state)
    submit_kyc.save()
    messages.success(request, 'Successfully saved')

    return render(request, 'kyc/(2nd)AccEmp.html')


def insertkyc(request):
    print("successfully completed")

    # variables of personal information
    global full_name, name_init, id_type, nics_no, driv_lic, driv_exp, pass_no, pass_exp, nationality
    global nationality_other, date_of_birth

    # variables of residential details
    global house_no, street, city, country

    # variables of contact information
    global mob_no, office, home, email_add

    # calling variables for form inputs in personal detail section
    full_name = request.POST["fullname"]
    name_init = request.POST["nwi"]
    id_type = request.POST["ID_type"]
    nics_no = request.POST["NIC"]
    driv_lic = request.POST["driving_license"]
    driv_exp = request.POST["drive_exp"]
    pass_no = request.POST["passport"]
    pass_exp = request.POST["passport_exp"]
    nationality = request.POST["Nationality"]
    nationality_other = request.POST["Nationality_other"]
    date_of_birth = request.POST["birthday"]

    # calling variables for form inputs in residential detail section
    house_no = request.POST["house_number"]
    street = request.POST["street"]
    city = request.POST["city"]
    country = request.POST["country"]

    # calling variables for form inputs in contact detail section
    mob_no = request.POST["mobile_number"]
    office = request.POST["office_number"]
    home = request.POST["home_number"]
    email_add = request.POST["email"]

    messages.success(request, 'Successfully saved')

    print(full_name)
    print(name_init)
    print(id_type)
    print(nics_no)

    # submit_kyc = Kyc_Info(full_name=full_name, name_init=name_init, id_type=id_type, nics_no=nics_no)
    # submit_kyc.save()
    # messages.success(request, 'Successfully submitted')

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
