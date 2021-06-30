from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):
	return render(request, 'index.html', {})

def about(request):
	return render(request, 'about.html', {})

def resume(request):
	return render(request, 'resume.html', {})

def service(request):
	return render(request, 'service.html', {})

def contact(request):
	if request.method == "POST":
		person_name = request.POST['name']
		person_email = request.POST['email']
		person_subject = request.POST['subject']
		person_text = request.POST['text']

		#send mail
		send_mail(person_subject, person_text, person_email, ['austinrossmoon571@gmail.com'])

		return render(request, 'contact.html', {})
	else:
		return render(request, 'contact.html', {})

