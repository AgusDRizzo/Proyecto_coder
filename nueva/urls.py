from django.urls import path
from nueva import views



urlpatterns = [
    path("paleta/<int:pk>/",views.PaletaDetailView.as_view(), name="paleta"),
    path("paleta/crear",views.PaletaCreateView.as_view(), name="paleta_crear"),
    path("paleta/<int:pk>/editar",views.PaletaUpdateView.as_view(), name="paleta_editar"),
    path("paleta/listar", views.PaletaListView.as_view(), name="paleta_listar"),
     path("paleta/<int:pk>/eliminar",views.PaletaDeleteView.as_view(), name="paleta_eliminar")
]
