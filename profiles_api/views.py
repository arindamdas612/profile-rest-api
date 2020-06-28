from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPIView(APIView):
    """Test API View"""

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