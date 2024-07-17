

from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path

from apps.forms import ProfileForm
from apps.views import RegisterFormView, CustomLoginView, CategoryListView, Prod, ProductList, ProfileFormView

urlpatterns = [
    path('', RegisterFormView.as_view()),
    path('login/', CustomLoginView.as_view(),name='login'),
    path('login/', LogoutView.as_view(),name='logout'),
    path('product/', CategoryListView.as_view(),name='product'),
    path('ca-pro/<str:slug>', Prod,name='ca-pro'),
    path('del-up/', ProductList.as_view(),name='del-up'),
    path('profile/', ProfileFormView.as_view(),name='profile'),
]
