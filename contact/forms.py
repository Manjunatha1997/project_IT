from django import forms

class SendEmail(forms.Form):
    sender = forms.EmailField(max_length=30)
    subject = forms.CharField(max_length=30)
    desc = forms.CharField(max_length=300, widget=forms.Textarea)
