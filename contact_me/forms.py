from django import forms
#Create your own forms below.

class ContactForm(forms.Form):
    name = forms.CharField(error_messages={'required': 'Please enter your name'})
    subject = forms.CharField(max_length = 100, error_messages={'required': 'Please enter a subject'})
    message = forms.CharField(widget = forms.Textarea, error_messages={'required': 'Please enter a message'})
    sender = forms.EmailField(error_messages={'required': 'Please enter your email'})
    cc_myself = forms.BooleanField(label = "CC myself?", required = False)

