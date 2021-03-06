"""bottlecaps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from bottlecaps import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', obtain_auth_token, name='login'),
    path('signup/', views.CreateUserView.as_view(), name='sign_up'),
    path('categories/', views.CategoryList.as_view(), name='categories'),
    path('titles/', views.TitleList.as_view(), name='titles'),
    path('titles-filter/', views.TitleFilteredList.as_view(), name='titles_filter'),
    path('title/<int:key>/', views.TitleView.as_view(), name='title'),
    path('reviews/', views.ReviewList.as_view(), name='reviews'),
    path('review/<int:key>/', views.ReviewView.as_view(), name='review'),
]
