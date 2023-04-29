"""
URL configuration for restaurant project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from restaurant.menu import views
from restaurant.menu.views import RestaurantViewSet, MenuViewSet, EmployeeViewSet

router = routers.DefaultRouter()
router.register(r'menu', views.MenuViewSet)
router.register(r'restaurant', views.RestaurantViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/v1/', include(router.urls)),
    path('api/v1/menu/', MenuViewSet.as_view({'get': 'list'})),
    path('api/v1/menu/<int:pk>/', MenuViewSet.as_view({'get': 'retrieve'})),
    path('api/v1/menu/today/', MenuViewSet.as_view({'get': 'today'})),
    path('api/v1/menu/rating/', MenuViewSet.as_view({'get': 'rating'})),
    path('api/v1/menu/<int:pk>/vote/', MenuViewSet.as_view({'post': 'vote'})),
    path('api/v1/restaurant/', RestaurantViewSet.as_view({'get': 'list'})),
    path('api/v1/restaurant/<int:pk>/', RestaurantViewSet.as_view({'get': 'retrieve'})),
    path('api/v1/restaurant/<int:pk>/menu/', MenuViewSet.as_view({'get': 'list'})),
    path('api/v1/restaurant/<int:pk>/menu/<int:menu_pk>/', MenuViewSet.as_view({'get': 'retrieve'})),
    path('api/v1/employee/', EmployeeViewSet.as_view({'get': 'list'})),
    path('api/v1/employee/<int:pk>/', EmployeeViewSet.as_view({'get': 'retrieve'})),
]

