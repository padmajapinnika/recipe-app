from django import forms

class RecipeSearchForm(forms.Form):
    CHART_CHOICES = [
        ('bar', 'Bar Chart'),
        ('pie', 'Pie Chart'),
        ('line', 'Line Chart'),
    ]

    query = forms.CharField(
        required=False,
        label='Search (by title or ingredient)',
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter recipe title or ingredient...',
            'style': 'width: 250px; padding: 0.3rem; border-radius: 4px; border: 1px solid #ccc;',
            'aria-label': 'Search recipes by title or ingredient'
        })
    )
    chart_type = forms.ChoiceField(
        choices=CHART_CHOICES,
        required=False,
        label='Chart Type',
        widget=forms.Select(attrs={
            'style': 'width: 140px; padding: 0.3rem; border-radius: 4px; border: 1px solid #ccc;',
            'aria-label': 'Select chart type'
        })
    )
