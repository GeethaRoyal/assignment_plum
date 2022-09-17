from django.urls import path
from . import views

urlpatterns = [
    path('organisations/', views.Organisations.as_view(), name='Organisations'),
    path('organisations/<int:org_id>/members/', views.MembersList.as_view(), name='Members'),
]