from django.contrib import admin
from django.urls import path

from . import views

app_name = "bank_finder_app"
urlpatterns = [
    path('', views.apphome, name="home"),
    path('branch/<str:ifsc_code>', views.BranchView.as_view(), name="branch"),
    path('branches/', views.BranchListView.as_view(), name="branches"),

]
