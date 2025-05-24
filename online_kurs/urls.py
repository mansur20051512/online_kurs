from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('online_kurs/', admin.site.urls),  # Django admin paneli uchun URL
    path('', include('kurslar.urls')),  # 'kurslar' ilovangizning URL’lari
]

# Agar DEBUG=True bo'lsa, media fayllarni lokal serverdan xizmat qilish uchun
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
