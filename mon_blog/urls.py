from django.contrib import admin
from django.urls import path
from users import views
from blog import views as blog_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),
    path('register/', views.register, name='register'),
    path('login_view/', views.login_view, name='login_view'),
    path('logout_view/', views.logout_view, name='logout_view'),
    path('articles/', blog_views.ArticleList.as_view(), name='article_list'),
    path('articles/<int:pk>/', blog_views.ArticleDetail.as_view(), name='article_detail'),
    path('articles/create/', blog_views.ArticleCreate.as_view(), name='article_create'),
    path('articles/<int:pk>/update/', blog_views.ArticleUpdate.as_view(), name='article_update'),
    path('articles/<int:pk>/delete/', blog_views.ArticleDelete.as_view(), name='article_delete'),
    path('categories/create/', blog_views.CategorieCreate.as_view(), name='categorie_create'),
    path('categories/<int:pk>/update/', blog_views.CategorieUpdate.as_view(), name='categorie_update'),
    path('categories/<int:pk>/delete/', blog_views.CategorieDelete.as_view(), name='categorie_delete'),
    path('dashboard/', blog_views.dashboard, name='dashboard'),
    path('administrateur/gestarticle/', blog_views.Gestarticle.as_view(), name='gestarticle'),
    path('administrateur/gestcategorie/', blog_views.Gestcategorie.as_view(), name='gestcategorie'),   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)