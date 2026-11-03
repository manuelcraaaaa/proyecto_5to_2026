from django.contrib import admin
from django.urls import path, include
from posts import views as post_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', post_views.lista_posts, name='lista_posts'),
    path('posts/<int:pk>/', post_views.detalle_post, name='detalle_post'),
    path('crear/', post_views.crear_post, name='crear_post'),
    path('historia/', include('historia.urls')),
    path('juegos/', include('juegos.urls')),

]

