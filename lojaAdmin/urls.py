
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('loja.urls.HomeUrls')),
    path('produto/', include('loja.urls.ProdutoUrls')),
    path('usuario/', include('loja.urls.UsuarioUrls')),
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)