from django.shortcuts import get_object_or_404
from rest_framework import status,generics
from rest_framework.views import APIView
from star.models import Star
from star.serializers import StarSerializer
from rest_framework.response import Response
class StarViewSet(generics.ListCreateAPIView):
    model = Star
    queryset = Star.objects.all()
    serializer_class = StarSerializer

class StarDetailView(APIView):
    def get(self, request, name):
        star = get_object_or_404(Star, name=name)
        serializer = StarSerializer(star)
        return Response(serializer.data)

    def delete(self, request, name):
        #star = get_object_or_404(Star, pk=pk)
        star = Star.objects.get(name=name)
        star.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    def put(self, request, pk):
        star = get_object_or_404(Star, pk=pk)
        serializer = StarSerializer(star, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

