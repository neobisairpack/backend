from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import *


class ServiceViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Service.objects.filter(is_checked=True)
    serializer_class = ServiceSerializer

    def list(self, request, *args, **kwargs):
        service = self.queryset.all()
        serializer = ServiceReadableSerializer(service, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save(requester=self.request.user)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request):
        pk = request.data.get('id', None)
        if pk is None:
            raise ParseError('Service id is required.')

        try:
            service = self.queryset.get(id=pk)
        except Service.DoesNotExist:
            raise Http404
        else:
            service.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class ServiceImageViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = ServiceImage.objects.all()
    serializer_class = ServiceImagesSerializer

    def get(self):
        image = self.queryset.all()
        serializer = self.serializer_class(image, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        pk = request.data.get('id', None)
        if pk is None:
            raise ParseError('Service id is required.')

        try:
            image = self.queryset.get(id=pk)
        except ServiceImage.DoesNotExist:
            raise Http404
        else:
            image.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class RequestServiceViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = RequestService.objects.all()
    serializer_class = RequestServiceSerializer

    def list(self, request, *args, **kwargs):
        service = self.queryset.all()
        serializer = RequestServiceReadableSerializer(service, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save(requester=self.request.user)

    def delete(self, request):
        pk = request.data.get('id', None)
        if pk is None:
            raise ParseError('Service id is required.')

        try:
            service = self.queryset.get(id=pk)
        except RequestService.DoesNotExist:
            raise Http404
        else:
            service.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class SupportViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Support.objects.all()
    serializer_class = SupportSerializer

    def list(self, request, *args, **kwargs):
        support = self.queryset.all()
        serializer = self.serializer_class(support, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request):
        pk = request.data.get('id', None)
        if pk is None:
            raise ParseError('Id is required')

        try:
            support = self.queryset.get(id=pk)
        except Support.DoesNotExist:
            raise Http404
        else:
            support.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class ProvideServiceViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = ProvideService.objects.filter(is_checked=True)
    serializer_class = ProvideServiceSerializer

    def list(self, request, *args, **kwargs):
        service = self.queryset.all()
        serializer = ProvideServiceReadableSerializer(service, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save(provider=self.request.user)

    def delete(self, request):
        pk = request.data.get('id', None)
        if pk is None:
            raise ParseError('Service id is required.')

        try:
            service = self.queryset.get(id=pk)
        except ProvideService.DoesNotExist:
            raise Http404
        else:
            service.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class ProvideServiceImageViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = ProvideServiceImage.objects.all()
    serializer_class = ProvideServiceImagesSerializer

    def get(self):
        image = self.queryset.all()
        serializer = self.serializer_class(image, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request):
        pk = request.data.get('id', None)
        if pk is None:
            raise ParseError('Service id is required.')

        try:
            image = self.queryset.get(id=pk)
        except ProvideServiceImage.DoesNotExist:
            raise Http404
        else:
            image.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class RequestProvideServiceViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = RequestProvideService.objects.all()
    serializer_class = RequestProvideServiceSerializer

    def list(self, request, *args, **kwargs):
        service = self.queryset.all()
        serializer = RequestProvideServiceReadableSerializer(service, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save(requester=self.request.user)

    def delete(self, request):
        pk = request.data.get('id', None)
        if pk is None:
            raise ParseError('Service id is required.')

        try:
            service = self.queryset.get(id=pk)
        except RequestProvideService.DoesNotExist:
            raise Http404
        else:
            service.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class ServiceFilterListAPIView(ListAPIView):
    queryset = Service.objects.filter(is_checked=True)
    serializer_class = ServiceReadableSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = [
        'status', 'deadline', 'service_type',
        'pickup_location', 'drop_off_location'
    ]
    search_fields = [
        'country', 'status', 'deadline', 'service_type',
        'pickup_location', 'drop_off_location'
    ]


class ProvideServiceFilterListAPIView(ListAPIView):
    queryset = ProvideService.objects.filter(is_checked=True)
    serializer_class = ProvideServiceReadableSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = [
        'status', 'deadline', 'service_type',
        'pickup_location', 'drop_off_location'
    ]
    search_fields = [
        'country', 'status', 'deadline', 'service_type',
        'pickup_location', 'drop_off_location'
    ]


class SupportFilterListAPIView(ListAPIView):
    queryset = Support.objects.all()
    serializer_class = SupportReadableSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'date']
