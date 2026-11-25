
from django import forms
from .models import Produce


class ProduceForm(forms.ModelForm):

    class Meta:
        model = Produce

        fields = [
            'name',
            'category',
            'quantity',
            'unit',
            'price_per_unit',
            'description',
        ]

        widgets = {
            'description': forms.Textarea(attrs={
                'rows': 3,
            }),
        }
