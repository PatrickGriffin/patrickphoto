from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadImageForm, ContactForm
from .models import UploadImage
from django.core.mail import send_mail
from django.conf import settings

def home(request):
	queryset = UploadImage.objects.filter(location='pictures')
	context = {
			'queryset':[]
		}
	for instance in queryset:
		context['queryset'].append(str(instance.image))

	return render(request, 'home_page_content.html', context)
# Create your views here.

def blog(request):
	queryset = UploadImage.objects.filter(location='blog')
	context = {
			'queryset':[]
		}
	for instance in queryset:

		context['queryset'].append(str(instance.image))

	return render(request, 'home_page_content.html', context)

def upload(request):
	print(request.method)
	if request.method == 'POST':
		image_form = UploadImageForm(request.POST, request.FILES)
		if(image_form.is_valid()):
			image_form.save()
			return HttpResponseRedirect('/')
	else:
		image_form = UploadImageForm()

		# if image_form.is_valid():
		# print(image_form.is_valid())
		# print(request.FILES)
	
	context = {
		"image_form":image_form,
	}
	
	return render(request, "upload.html", context)	

def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		# do stuff
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_full_name = form.cleaned_data.get("full_name")
		subject = 'Site contact form'
		from_email = settings.EMAIL_HOST_USER
		to_email = ['p2dag2@gmail.com'] #put in form_email in future
		contact_message = """
		%s:%s via %s
		"""%(form_full_name, form_message, form_email)

		send_mail(subject, 
				contact_message, 
				from_email,
		    	to_email, 
		    	fail_silently=False)
	
	context = {
		"form":form,
	}
	return render(request, "contact.html", context)