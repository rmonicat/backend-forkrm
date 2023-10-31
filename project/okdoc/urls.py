from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('medico.urls')),
    path('usuarios/', include('django.contrib.auth.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/docs/', SpectacularSwaggerView.as_view(url_name='schema')),
    path('', include('tryasync.urls')),
]
a = 9
