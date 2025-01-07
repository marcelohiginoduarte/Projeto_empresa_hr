from django.contrib import admin
from django.urls import path, include
from GestaoHR.views import home
from django.conf.urls.static import static 
from django.conf.urls import handler403
from django.conf import settings
from django.contrib.auth import views as auth_views
from GestaoHR.views import permission_denied_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='homapage'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('demandainterna/', include('demandainterna.urls')),
    path('servico/', include('Servico.urls')),
    path('equipe', include('Equipe.urls')),
    path('arquivo', include('Arquivo.urls')),
    path('colaboradores', include('GestaoHR.urls')),
    path('fotoscampo', include('Fotoscampo.urls')),
    path('sesmt', include('Sesmt.urls')),
    path('estoque', include('Estoque.urls')),
    path('programacao', include('Programacao.urls')),
    path('bancoarquivo', include('Bancoarquivos.urls')),

    
    
]
handler403 = permission_denied_view
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

