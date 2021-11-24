from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("main.urls")),
    path("accounts/", include("allauth.urls")),
    path("mypage/", include("mypage.urls")),
    path("donation/", include("donation.urls")),
    path("quiz/", include("quiz.urls"))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)