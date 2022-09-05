from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .actions import get_info
from .exception import Custom_exception
from .serializers import Band_or_artist_name, Band_or_artist_response_data

from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
# Create your views here.

class Band_or_artis_info(APIView):
    """
    Get method view to return artist informaition.
    """
    @method_decorator(cache_page(120))
    def get(self, request):
        name = Band_or_artist_name(data=request.query_params)
        name.is_valid(True)
        name = name.data.get('name')

        try:
            info = get_info(name=name)
        except Custom_exception as err:
            return Response (status=status.HTTP_400_BAD_REQUEST, data={"error_id":err.error_id, "mesagge":err.message})

        response_data = Band_or_artist_response_data(data=info)
        response_data.is_valid(True)

        return Response (status=status.HTTP_200_OK, data=response_data.validated_data)