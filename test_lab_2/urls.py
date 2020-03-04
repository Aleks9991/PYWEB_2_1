from django.urls import path
from test_lab_2.views import LoginView

urlpatterns = [
    path('', LoginView.as_view()),
]