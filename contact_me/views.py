from django.shortcuts import render
from django.http  import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError

# Create your views heres

def contact_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']
            recipients = ['deepcellVision@gmail.com']
            message = "From " + name + ": \n" + message
            if cc_myself:
                recipients.append(sender)
            try:
                send_mail(subject, message, sender, recipients)
            except BadHeaderError:
                return HttpResponseRedirect('invalid/')
            return HttpResponseRedirect('thanks/')
    else:
        form = ContactForm()
	context_data = {'form': form}
    return render(request, 'contact_me/contact.html', {'form': form})

def thanks(request):
    return render(request, 'contact_me/thanks.html')

def invalid(request):
    return render(request, 'contact_me/invalid.html')
