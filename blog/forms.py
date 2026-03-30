from django import forms
from .models import Article, Categorie
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['headline', 'categorie', 'content', 'image', 'status']
        widgets = {
            'headline': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre de l\'article', 'required': True}),
            'categorie': forms.Select(attrs={'class': 'form-select', 'required': True}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Contenu de l\'article'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de la catégorie', 'required': True}),
        }        