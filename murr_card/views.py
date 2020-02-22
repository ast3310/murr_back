from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from server_settings.common import base_frontend_url, base_backend_url
from .serializers import MurrCardSerializers, EditorImageForMurrCardSerializers, EditorDataForMurrSerializers
from .models import MurrCard, EditorDataForMurrCard


class MurrCardView(APIView):

    def get(self, request):
        qs = MurrCard.objects.all()
        serializer = MurrCardSerializers(qs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MurrCardSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class EditorImageForMurrCardView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = EditorImageForMurrCardSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            url = base_backend_url + serializer.data['murr_editor_image']
            murr_dict = {"success": 1, "file": {"url": url}}

            return Response(murr_dict)

        else:

            murr_dict = {"success": 0, "file": {"url": ""}}
            return Response(murr_dict)


class EditorDataForMurrView(APIView):
    # permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = EditorDataForMurrSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        else:
            return Response(serializer.errors)

    def get(self, request):
        r = EditorDataForMurrCard.objects.get(id=request.query_params['murr_id'])
        serializer = EditorDataForMurrSerializers(r)
        return Response(serializer.data)
