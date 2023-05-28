from django.shortcuts import render
from rest_framework.views import APIView, status
from rest_framework.response import Response
from django.forms.models import model_to_dict
from .models import Team
from .utils import data_processing
from .exceptions import NegativeTitlesError
from .exceptions import InvalidYearCupError
from .exceptions import ImpossibleTitlesError


class TeamsView(APIView):
    def post(self, request):
        try:
            data_processing(request.data)
        except NegativeTitlesError as e:
            return Response({"error": e.message}, status.HTTP_400_BAD_REQUEST)
        except InvalidYearCupError as e:
            return Response({"error": e.message}, status.HTTP_400_BAD_REQUEST)
        except ImpossibleTitlesError as e:
            return Response({"error": e.message}, status.HTTP_400_BAD_REQUEST)
        req = Team.objects.create(**request.data)
        resToDict = model_to_dict(req)
        return Response(resToDict, status.HTTP_201_CREATED)

    def get(self, request):
        listRes = []
        res = Team.objects.all()

        listRes = [model_to_dict(resDict) for resDict in res]
        return Response(listRes, status.HTTP_200_OK)
