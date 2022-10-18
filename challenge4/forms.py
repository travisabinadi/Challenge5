from django import forms
from .models import PortfolioItem

class PortfolioItemForm(forms.ModelForm):
    class Meta:
        model = PortfolioItem
        fields = ['item_name', 'item_description', 'item_image']

