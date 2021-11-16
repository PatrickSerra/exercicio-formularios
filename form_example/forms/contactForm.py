from django import forms
from .validators import validate_lowercase
from django.core.exceptions import ValidationError
class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, validators={validate_lowercase})
    message = forms.CharField(widget=forms.Textarea)
    cc_myself = forms.BooleanField(required=False, label="Send to myself")
    sender = forms.EmailField(required=False, help_text="who you are sending this email")

    
    def clean_message(self):
        value = self.cleaned_data['message']
        if value.lower() != value:
            raise ValidationError("{} is not lowercase".format(value))
        
        return value

    def clean(self):
        cleaned_data = super().clean()
        
        if cleaned_data['cc_myself'] and not cleaned_data.get("sender"):
            self.add_error("sender", "The sender is required to myself´s emails")
    
    