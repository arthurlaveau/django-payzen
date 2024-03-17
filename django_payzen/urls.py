from django.urls import path

from . import views

urlpatterns = [
        path("response/", views.ResponseView.as_view(), name="django_payzen_response"),
]
