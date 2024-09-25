from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/blog/', include('blog.urls')),           # Include blog app URLs
    path('api/departments/', include('departments.urls')),  # Include departments app URLs
]