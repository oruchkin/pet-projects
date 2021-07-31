from django.shortcuts import render
from . models import ClaimStatus, Claim

# Create your views here.

def getClaimsData(request):
    all_claim_data = Claim.objects.all()

    return render(request, "claims/claimdata.html",{
        "all_claim_data": all_claim_data
    })
