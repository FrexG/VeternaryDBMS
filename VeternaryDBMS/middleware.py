from home.models import Profile
from django.shortcuts import redirect


class GetUserMiddleware:
    VET_ACCESS = ['register','regular', 'clinicalservice',
                  'parasitetreatment','vaccination',
                  'abattoir_exam','lab_exam','logout']

    CASHIER_ACCESS = ['logout','cashier']

    PHARMACIST_ACCESS = ['logout','pharmacy']

    STOCK_ACCESS = ['logout','drug_in_out','drug_in_out/drugout','equipment_in_out/equipmentin',
                    'equipment_in_out/equipmentout','vaccine_in_out/vaccinein','vaccine_in_out/vaccineout',
                    'receipt_in_out','receipt_in_out/receipt_out']
    
    ADMIN_ACCESS = list(set(VET_ACCESS +CASHIER_ACCESS)) + ['dashboard']

    print(ADMIN_ACCESS)

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, *args, **kwargs):
        # get role of each loged in user

        if str(request.user) != "AnonymousUser":
            role = Profile.objects.get(user=request.user).role
            path = request.path.strip('/')
            print(f"Path: {request.path}")
            print(f"Striped Path: {path}")

            # If user is logged in as a Veternerian
            if str(role) == 'Vet' and path not in self.VET_ACCESS:
                return redirect("/regular")
            # If user is logged in as a Cashier
            if str(role) == 'Cashier' and path not in self.CASHIER_ACCESS:
                return redirect("/cashier") 
            # If user is logged in as a Pharmacist
            if str(role) == 'Pharmacist' and path not in self.PHARMACIST_ACCESS: 
                return redirect("/pharmacy")
            # If user is logged in as a Stock Keeper
            if str(role) == 'Stock_Keeper' and path not in self.STOCK_ACCESS:
                return redirect("/drug_in_out")
            
            
        


