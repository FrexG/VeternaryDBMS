from home.models import Profile
from django.shortcuts import redirect

VET_ACCESS = ['regular', 'clinicalservice', 'parasite&vaccination']
CASHIER_ACCESS = ['register']
ADMIN_ACCESS = VET_ACCESS + CASHIER_ACCESS


class GetUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print(get_response)

    def __call__(self, request):
        if str(request.user) != "AnonymousUser":
            self.__process_permission(request)
        response = self.get_response(request)
        return response

    def __process_permission(self, request):
        # get role of each loged in user
        role = Profile.objects.get(user=request.user).role
        path = request.path.strip('/')

        if str(role) == 'Vet':
            print(str(role))
            if path in VET_ACCESS:
                print("Can access")
            else:
                return redirect("/")
        print(path)
