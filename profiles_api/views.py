from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions



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


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self, rquest):
        """Return a Hello Message"""
        a_viewset = [
            'uses action (list, create, retrieve, update, partial update)',
            'Automatically maps to URLs using router',
            'Provides more functionality',
        ]

        return Response({
            'message': 'Hello', 
            'a_viewset': a_viewset
        })

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            return Response({
                'message': f"Hello {name}"
            })
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({"http_method": "get"})

    def update(self, request, pk=None):
        """Handle updating an object by its ID"""
        return Response({"http_method": "put"})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object by its ID"""
        return Response({"http_method": "patch"})

    def destroy(self, request, pk=None):
        """Removing an object by its ID"""
        return Response({"http_method": "delete"})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
