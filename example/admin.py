from django.contrib import admin
from django import forms

from .models import Article, Tag


class ArticleCreationForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ("title", "tags")
        widgets = {
            "tags": forms.SelectMultiple,
        }


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    model = Article
    add_form = ArticleCreationForm
    form = ArticleCreationForm


admin.site.register(Tag)
