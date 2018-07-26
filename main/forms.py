from django import forms
from main.models import ContactForm

class ContactFormF(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['username', 'email', 'message']

