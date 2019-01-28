from django import forms

class SearchForm(forms.Form):
    search_query = forms.CharField(
                        max_length=100,
                        label='',
                        widget=forms.TextInput(attrs={'class':'form-control',
                                                'placeholder':'Search for...',
                                                }
                        ),
                    )