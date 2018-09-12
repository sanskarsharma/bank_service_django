from django.http import HttpResponse, HttpResponseRedirect

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *

import json
from .models import Banks, Branches
from .serializers import BanksSerializer, BranchesSerializer


def apphome(request):

    banks = Banks.objects.first()
    response_dict = {}
    response_dict["bankee"] = banks.name
    return HttpResponse(json.dumps(response_dict))


class BranchView(APIView):

    def get(self, request, ifsc_code):

        """ GET - get details of a brank branch by IFSC code"""

        response_dict = {}

        branch = Branches.objects.filter(ifsc=ifsc_code).first()
        if branch is None:
            response_dict["message"] = "no branch with this ifsc code found"
            return Response(response_dict, status=HTTP_404_NOT_FOUND)

        branch_serialized = BranchesSerializer(branch).data
        return Response(branch_serialized)


class BranchListView(APIView):

    def get(self, request):

        """ GET - get all branches of a BANK in a CITY """

        response_dict = {}
        city = request.GET.get("city", None)
        bank_name = request.GET.get("bank_name", None)

        bank = Banks.objects.filter(name=bank_name.upper()).first()
        if bank is None:
            response_dict["message"] = "Bank with given bank_name does not exist"
            return Response(response_dict, status=HTTP_422_UNPROCESSABLE_ENTITY)

        branches = Branches.objects.filter(city=city.upper(), bank=bank)

        if len(branches) < 1:
            response_dict["message"] = "no branch of {} exists in {}".format(bank_name, city)
            return Response(response_dict, status=HTTP_404_NOT_FOUND)

        branches_serialized = BranchesSerializer(branches, many=True).data
        return Response(branches_serialized)

