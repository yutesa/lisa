from yutesapp.models import Products
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from yutesapp.forms import LikeForm

def inicio(request):
	if request.method=='POST':
		formulario = UserCreationForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = UserCreationForm()
	return render_to_response('inicio.html', {'formulario':formulario}, context_instance=RequestContext(request))

def Productos(request):
	formsito = LikeForm()
	AllProducts = Products.objects.all()[:10]
	return render_to_response('Products.html', {'datos':AllProducts, 'frmAddLike':formsito}, context_instance=RequestContext(request))

def DarLike(request):
	if request.is_ajax():
		if request.method == 'POST':
			form = LikeForm(data=request.POST)
			if form.is_valid():
				u = form.save()

				respuesta = {'codigo': 1, 'msg': 'La ubicacion fue guardada'}
				return HttpResponse(simplejson.dumps(respuesta))
			else:
				respuesta = {'codigo': 2, 'msg': 'Faltan datos'}
				return HttpResponse(simplejson.dumps(respuesta))
	# if request.method == 'POST':
	# 	Formi = LikeForm(request.POST)
	# 	if Formi.is_valid():
	# 		Formi.save()
	# 		return HttpResponseRedirect('/ya/')
	# 	else:
	# 		return HttpResponseRedirect('/error/')