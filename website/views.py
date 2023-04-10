from django.shortcuts import render
from datetime import datetime
from website.models import Contact
from django.contrib import messages 

# Create your views here.
def index(request):
    return render(request, "index.html")

def works(request):
    return render(request, "works.html")

def about(request):
    return render(request, "about.html")  

def contact(request):
    if request.method == "POST":
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = Contact(email=email, subject=subject, message=message, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent.')
    return render(request, "contact.html")

def home(request):
    return render(request, "index.html")

def contact_form(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact request submitted successfully.')
            return render(request, 'contact-form.html', {'form': ContactForm(request.GET)})
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)
    else:
        form = ContactForm()
    return render(request, 'contact-form.html', {'form': form})