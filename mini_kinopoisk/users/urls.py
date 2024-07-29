from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from users.views import profile, login, registration, logout


app_name = "users"


urlpatterns = [
    path("profile/", profile, name="profile"),
    path("login/", login, name="login"),
    path("registration/", registration, name="registration"),
    path("logout/", logout, name="logout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
