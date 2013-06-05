#-*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from models import *
from forms import *
from Teatre.urls import *
from serializers import *
from rest_framework import generics, permissions

def mainpage(request):

	template = get_template('index.html')
	variables = Context({
		'titlehead': 'Teatre aPP',
		'pagetitle': 'Benvingut a la aplicació de Teatres',
		'contentbody': 'Aquí podràs administrar coses de Teatre',
		'user': request.user,
	})
	output = template.render(variables)
	return HttpResponse(output)


# ERROR, in logging
class LoginRequiredMixin(object):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


class CheckIsOwnerMixin(object):
    def get_object(self, *args, **kwargs):
        obj = super(CheckIsOwnerMixin, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise PermissionDenied
        return obj


def error(request):
	template = get_template('error.html')
	variables = Context({
		'pagetitle': "No t'has autenticat",
	})
	output = template.render(variables)
	return HttpResponse(output)

#--------------------------------------------Generic classes------------------------------------------------

#CREATE
class GenericCreate(LoginRequiredMixin,CreateView): 
	
	def form_valid(self, form): 
		form.instance.user = self.request.user
		return super(GenericCreate, self).form_valid(form)
 


#DETAIL
class GenericDetail(DetailView):

	def get_context_data(self, **kwargs):
		context = super(GenericDetail, self).get_context_data(**kwargs)
		return context

#DETAIL REPRESENTACIO
class RepresentacioDetail(DetailView):
    model = Representacio
    template_name = 'representacio.html'

    def get_context_data(self, **kwargs):
        context = super(RepresentacioDetail, self).get_context_data(**kwargs)
        context['RATING_CHOICES'] = RepresentacioReview.RATING_CHOICES
        return context

# EDIT
class GenericUpdate(LoginRequiredMixin,CheckIsOwnerMixin, UpdateView):
	
	pass


# DELETE
class GenericDelete(LoginRequiredMixin,CheckIsOwnerMixin,DeleteView):
	pass



@login_required()
def review(request, pk):
    representacio = get_object_or_404(Representacio, pk=pk)
    review = RepresentacioReview(
        rating=request.POST['rating'],
        comment=request.POST['comment'],
        user=request.user,
        representacio=representacio)
    review.save()
    return HttpResponseRedirect(reverse('representacio_detail', args=(representacio.id,)))
	
	
#APIS
class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.user == request.user


#Escriptor
class APIEscriptorList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Escriptor
    serializer_class = EscriptorSerializer

class APIEscriptorDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Escriptor
    serializer_class = EscriptorSerializer

#Actor
class APIActorList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Actor
    serializer_class = ActorSerializer

class APIActorDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Actor
    serializer_class = ActorSerializer


#Director
class APIDirectorList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Director
    serializer_class = DirectorSerializer

class APIDirectorDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Director
    serializer_class = DirectorSerializer

#Representacio
class APIRepresentacioList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Representacio
    serializer_class = RepresentacioSerializer

class APIRepresentacioDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Representacio
    serializer_class = RepresentacioSerializer

#Obra Teatre
class APIObra_TeatreList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Obra_Teatre
    serializer_class = Obra_TeatreSerializer

class APIObra_TeatreDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Obra_Teatre
    serializer_class = Obra_TeatreSerializer


#nom_Obra
class APInom_ObraList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = nom_Obra
    serializer_class = nom_ObraSerializer

class APInom_ObraDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = nom_Obra
    serializer_class = nom_ObraSerializer


