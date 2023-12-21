from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def getData(request):
    test_data = {"name": "Testing"}
    return Response(test_data)