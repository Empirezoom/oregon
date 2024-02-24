from .models import *




def oregon(request):
    profile = CompanyProfile.objects.get(pk=1)

    context = {
        'profile': profile,
    }

    return context