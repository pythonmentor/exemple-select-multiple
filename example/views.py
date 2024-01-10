from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from .models import Article
from .forms import ArticleCreationForm


class ArticleListView(ListView):
    model = Article
    template_name = "example/index.html"


class ArticleChangeView(UpdateView):
    model = Article
    form_class = ArticleCreationForm
    success_url = reverse_lazy("home")
    template_name = "example/update.html"
