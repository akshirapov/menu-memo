from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from pantry.apps.users import views as user_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", user_views.UserRegisterView.as_view(), name="register"),
    path("login/", user_views.UserLoginView.as_view(), name="login"),
    path("logout/", user_views.UserLogoutView.as_view(), name="logout"),
    path("", include("pantry.apps.recipes.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
