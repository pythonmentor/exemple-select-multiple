from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field

from .models import Article


class ArticleCreationForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ("title", "tags")
        widgets = {
            "tags": forms.SelectMultiple,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            "title",
            Field("tags", template="tailwind/multiple_select.html"),
        )
