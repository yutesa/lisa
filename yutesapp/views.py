from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

def inicio(request):
	if request.method=='POST':
		formulario = UserCreationForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = UserCreationForm()
	return render_to_response('inicio.html', {'formulario':formulario}, context_instance=RequestContext(request))

def Products(request):
	return render_to_response('Products.html', context_instance=RequestContext(request))