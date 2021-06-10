from home.models import Profile
from django.shortcuts import redirect


class GetUserMiddleware:
    VET_ACCESS = ['regular', 'clinicalservice',
                  'parasite&vaccination', 'logout']
    CASHIER_ACCESS = ['register', 'logout']
    ADMIN_ACCESS = VET_ACCESS + CASHIER_ACCESS

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, *args, **kwargs):
        # get role of each loged in use

        if str(request.user) != "AnonymousUser":
            role = Profile.objects.get(user=request.user).role
            path = request.path.strip('/')

            # If user is logged in as a Veternerian
            if str(role) == 'Vet' and path not in self.VET_ACCESS:
                return redirect("/regular")
            # If user is logged in as a Cashier
            if str(role) == 'Cashier' and path not in self.CASHIER_ACCESS:
                return redirect("/register")
            # grant the admin access to all pages
