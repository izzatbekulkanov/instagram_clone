from django.urls import path
from .serializers import SignUpSerializer
from .views import CreateUserView

urlpatterns = [
    path('singup/', CreateUserView.as_view())
]
