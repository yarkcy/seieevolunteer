from django.shortcuts import render_to_response
from event.models import Event,DateTime
from people.models import People
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
def index(request):
	return render_to_response('index.html')

def signup(request):
	return render_to_response('signup.html',{'events':Event.objects.all()})

def sign_info(request):
	ID = request.path[11:]
	ID = int(ID)
	p = Event.objects.get(id=ID)
	return render_to_response('sign_info.html',{'event':p},context_instance=RequestContext(request))

def signup_info_back(request):
	errors = []
	if request.method =='POST':
		if not request.POST.get('name',''):
			errors.append('Enter a subject.')
		if not request.POST.get('student_id',''):
			errors.append('Enter a id.')
		if not request.POST.get('phone',''):
			errors.append('Enter a phone number.')
		if not errors:
			ID = request.path[18:]
			ID = int(ID)
			p1 = Event.objects.filter(id=ID)
			p2 =People.objects.create(name=request.POST['name'],
				student_id=request.POST['student_id'],phone=request.POST['phone'])
			p2.event=p1
			return HttpResponseRedirect('/signup/thanks/')
	return render_to_response('sign_info.html',{'errors':errors},context_instance=RequestContext(request))

def thanks(request):
	return render_to_response('thanks.html')

def lookup(request):
	return render_to_response('lookup.html',context_instance=RequestContext(request))

def lookup_result(request):
	errors = []
	results=''
	if request.method =='POST': 
		if not request.POST.get('student_id',''):
			errors.append('Enter a id.')
		if not errors:
			ID = request.POST['student_id']
			try:
				p = People.objects.get(student_id=ID)
				results =  p.event.all()
			except People.DoesNotExist:
				results = 'this id is not existed'

	return render_to_response('lookup.html',{'results':results},context_instance=RequestContext(request))

def contact(request):
	return render_to_response('contact.html',context_instance=RequestContext(request))

def contact_reply(request):
	errors = []
	if request.method == 'POST':
		if not request.POST.get('message',''):
			errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            send_mail(
                request.POST['email'],
                request.POST['message'],
                request.POST.get('email', 'noreply@example.com'),['582331715@qq.com'],)
            return HttpResponseRedirect('/contact/thanks/')
        return render_to_response('contact.html', {
    	'errors': errors,
    	'subject': request.POST.get('subject', ''),
    	'message': request.POST.get('message', ''),
    	'email': request.POST.get('email', ''),
    },context_instance=RequestContext(request))