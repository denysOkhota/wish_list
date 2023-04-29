from datetime import date

from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import RestaurantSerializer, MenuSerializer, EmployeeSerializer
from .models import Restaurant, Menu, Employee


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = self.queryset
        pk = self.kwargs.get('pk')
        if pk:
            queryset = queryset.filter(id=pk)
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return RestaurantSerializer
        return RestaurantSerializer

    def perform_create(self, serializer):
        if 'pk' in self.kwargs:
            serializer.save(id=self.kwargs['pk'])
        else:
            serializer.save()


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = self.queryset
        pk = self.kwargs.get('pk')
        if pk:
            queryset = queryset.filter(id=pk)
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return MenuSerializer
        return MenuSerializer

    def perform_create(self, serializer):
        if 'pk' in self.kwargs:
            serializer.save(id=self.kwargs['pk'])
        else:
            serializer.save()

    @action(detail=False, methods=['get'])
    def today(self, request):
        menus = Menu.objects.filter(date=date.today())
        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def vote(self, request, pk=None):
        menu = self.get_object()
        menu.votes += 1
        menu.save()
        serializer = MenuSerializer(menu)
        return Response(serializer.data)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = self.queryset
        pk = self.kwargs.get('pk')
        if pk:
            queryset = queryset.filter(id=pk)
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return EmployeeSerializer
        return EmployeeSerializer

    def perform_create(self, serializer):
        if 'pk' in self.kwargs:
            serializer.save(id=self.kwargs['pk'])
        else:
            serializer.save()
