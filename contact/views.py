from django.shortcuts import render
from contact.forms import *
from django.core.mail import send_mail

# Create your views here.
def contact_us(request):
    form = SendEmail()
    if 'sender' in request.GET:
        sender = request.GET['sender']
        subject = request.GET['subject']
        desc = request.GET['desc']
        print(sender, subject, desc)
        send_mail(subject, desc, sender, ['django.training.2019@gmail.com', 'pythontraining.blr@gmail.com'])
    return render(request, "contact/email.html", {'form': form})