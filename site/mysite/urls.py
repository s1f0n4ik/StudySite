from django.contrib import admin
from django.urls import path
from django.conf import settings             # Импортируем settings
from django.conf.urls.static import static # Импортируем static

urlpatterns = [
    path('admin/', admin.site.urls),
]

# Добавляем этот блок для раздачи медиафайлов в режиме разработки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)