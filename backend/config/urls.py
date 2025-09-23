from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin do Django
    path('admin/', admin.site.urls),

    # Endpoints do Djoser (auth/login, registro etc)
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

    # Suas APIs
    path('api/', include('quizapp.urls')),
    path('api/', include('users.urls')),
    path('api/', include('progress.urls')),  # <-- sua nova API de progresso
]
