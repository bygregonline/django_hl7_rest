

from django import forms
FORMATS = [
    ('json', 'json'),
    ('xml', 'xml'),
    ('yaml', 'yaml'),
    ('html', 'html'),
    ('txt', 'txt'),
]


class Simple_submit_Form(forms.Form):

    data = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'autocomplete': 'off', 'placeholder': 'hl7 message'}))

    """[summary]
    """
    format = forms.ChoiceField(
        choices=FORMATS, widget=forms.Select(attrs={'class': 'form-control'}))
