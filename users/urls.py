from django.urls import path
from .views import CreateUserView, VerifyAPIView, GetNewVerification, ChangeUserInformationView, \
    ChangeUserPhotoSerializerView, LoginView, LoginRefreshView, LogoutView, ForgotPasswordView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('refresh/', LoginRefreshView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('signup/', CreateUserView.as_view()),
    path('verify/', VerifyAPIView.as_view()),
    path('new-verify/', GetNewVerification.as_view()),
    path('change-user/', ChangeUserInformationView.as_view()),
    path('change-user-photo/', ChangeUserPhotoSerializerView.as_view()),
    path('forgot/', ForgotPasswordView.as_view()),

]
