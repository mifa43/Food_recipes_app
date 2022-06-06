"""foodApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from foodRecipes.views import HomeView, GetRecipe, Register, SearchView
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomeView.as_view(), name="home"),
    path('get-recipes/', GetRecipe.as_view(), name="get-recipes"),
    path('view-search/', SearchView.as_view(), name="view-search"),

    path('search/', views.searchRecipe, name='search'),
    path('food/', views.getRecipes, name="food"),
    path('post-recipe/', views.postRecipes, name="post-recipe"),
    path('post-clearbit-data/', views.clearBitApi, name="post-clearbit-data"),
    path("", include("django.contrib.auth.urls")),
    path('test/', views.Auth.as_view(), name='test'),
    # path('post-rating/', views.postRecipes, name="post-rating"), 
    path("register/", Register.as_view(), name="registerForm" ),
    path('account/register', views.register, name="register"),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns = format_suffix_patterns(urlpatterns)