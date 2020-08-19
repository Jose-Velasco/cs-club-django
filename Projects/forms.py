from django import forms

class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=50)
    subject = forms.CharField(max_length=250, widget=forms.Textarea)