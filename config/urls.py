from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
   path('admin/', admin.site.urls),
   path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
   path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
   path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
   path('api/auth/', include('authentication.urls')),
   path('api/snippets/', include('snippets.urls')),
   path('api/technologies/', include('technologies.urls')),
]
