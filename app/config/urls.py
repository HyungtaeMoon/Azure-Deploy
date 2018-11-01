from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import render
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: render(request, 'root.html'), name='root'),
]
# + static(
#     prefix=settings.MEDIA_URL,
#     document_ROOT=settings.MEDIA_ROOT
# )

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
