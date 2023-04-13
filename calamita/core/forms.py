from django import forms


class LocationForm(forms.Form):

    title = forms.CharField(label='заголовок', max_length=20, required=True)
    category = forms.CharField(label='категория', max_length=20, required=True)
    description = forms.CharField(label='описание', max_length=500)
    images = forms.FileField(label='изображения', widget=forms.ClearableFileInput(attrs={'multiple': True}))
    longitude = forms.FloatField(widget=forms.HiddenInput(attrs={'class': 'longitude'}), required=True)
    latitude = forms.FloatField(widget=forms.HiddenInput(attrs={'class': 'latitude'}), required=True)
