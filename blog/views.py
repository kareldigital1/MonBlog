from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Categorie
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



# Create  views of Article.
# afficher la liste des articles
class ArticleList(ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'articles'

# afficher les details d'un article
class ArticleDetail(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'article'

# creer un article
class ArticleCreate(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article_form.html'
    fields = ['headline', 'content', 'image', 'status', 'categorie']
    success_url = '/dashboard/'

# modifier un article
class ArticleUpdate(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = 'article_form.html'
    fields = ['headline', 'content', 'image', 'status', 'categorie']
    success_url = '/dashboard/' 

# supprimer un article
class ArticleDelete(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = '/dashboard/'


# Create  views of Categorie.
#creer une categorie
class CategorieCreate(LoginRequiredMixin, CreateView):
    model = Categorie
    template_name = 'categorie_form.html'
    fields = ['name']
    success_url = '/dashboard/'

# modifier une categorie
class CategorieUpdate(LoginRequiredMixin, UpdateView):
    model = Categorie
    template_name = 'categorie_form.html'
    fields = ['name']
    success_url = '/dashboard/'

# supprimer une categorie
class CategorieDelete(LoginRequiredMixin, DeleteView):  
    model = Categorie
    template_name = 'categorie_delete.html'
    success_url = '/dashboard/'    

class Gestarticle(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'administrateur/gestarticle.html'
    context_object_name = 'articles'

class Gestcategorie(LoginRequiredMixin, ListView):
    model = Categorie
    template_name = 'administrateur/gestcategorie.html'
    context_object_name = 'categories'


# dashboard view
@login_required
def dashboard(request):
    nb_articles = Article.objects.count()
    nb_categories = Categorie.objects.count()
    
    context = {
        'nb_articles': nb_articles,
        'nb_categories': nb_categories,
    }
    return render(request, 'dashboard.html', context)

