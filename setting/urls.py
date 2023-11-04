from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Instagram clone API",
        default_version="V1",
        description="""
        instagram clone
        add post
        create coment
        like comment
        like post
        """,
        terms_of_service="demo.com",
        contact=openapi.Contact(email="izzatbekulkanov@gmail.com"),
        license=openapi.License(name="demo Licence"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)

urlpatterns = [
    path('admin/', admin.site.urls),  # Django administrator paneli

    # 'users' ilovasi uchun URL konfiguratsiyasi
    path('users/', include('users.urls')),

    # 'post' ilovasi uchun URL konfiguratsiyasi
    path('post/', include('post.urls')),

    # Swagger va ReDoc API dokumentatsiyasi yo'nalishlari
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc')
]
