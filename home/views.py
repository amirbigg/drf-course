from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def one(request):
	return Response({'name':'amir'})