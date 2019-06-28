from django.contrib import admin
from django.urls import path, include
from api.routers import router as profile_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(profile_router.urls)),  # Profiles routers
]
