from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from profiles_api import serializers


class HelloAPIView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of API View Features"""
        an_apiview = [
            'uses HTTP methods as function (get, post, patch, put, delete)',
            'Is Similar to traditional Django View',
            'Gives you the most control over your application logic',
            'is mapped manually to URLs',
        ]

        return Response({
            'message': 'Hello', 
            'an_apiview': an_apiview
        })
    
    def post(self, request):
        """Create a hellow message with out name"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            msg = f"Hello {name}"
            return Response({'message': msg})
        else:
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updateing an object"""
        return Response({'mehtod': 'put'})


    def patch(self, request, pk=None):
        """Handle upartial update of an object"""
        return Response({'mehtod': 'patch'}) 

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'mehtod': 'dekete'}) 