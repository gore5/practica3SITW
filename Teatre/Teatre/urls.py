from django.conf.urls import patterns, include, url
from iTeatre.views import *
from django.views.generic import DetailView, ListView, UpdateView 
from iTeatre.forms import *
from iTeatre.models import *
from django.utils import timezone
from rest_framework.urlpatterns import format_suffix_patterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

	url(r'^$', mainpage, name='home'),

#-------------------------------------------------ESCRIPTOR-----------------------------------------------

	# LIST
	url(r'^escriptors$', ListView.as_view(queryset=Escriptor.objects.filter(),context_object_name='contentbody', template_name='llista.html'), name='escriptor_list'),

	# UPDATE
	url(r'^escriptors/(?P<pk>\d+)/edit/$', GenericUpdate.as_view(
	model = Escriptor,
	template_name = 'form.html', 
	form_class = EscriptorForm), 
	name='update_escriptor'),

	# CREATE
	url(r'^escriptors/create/$', GenericCreate.as_view(
	model =  Escriptor,
	template_name = 'form.html',
	form_class = EscriptorForm), 
	name='escriptor_create'),
	
	# DETAIL
	url(r'^escriptors/(?P<pk>\d+)/$',GenericDetail.as_view(
	model = Person,
	template_name = 'dades.html'), 
	name='escriptor_detail'),

	# DELETE
	url(r'^escriptors/(?P<pk>\d+)/delete/$',GenericDelete.as_view(
	model = Escriptor,
	template_name = 'form.html', 
	success_url = '/escriptors'),
	name='escriptor_delete'),

#-------------------------------------------------ACTOR-----------------------------------------------
	
	# LIST
	url(r'^actors$', ListView.as_view(queryset=Actor.objects.filter(),context_object_name='contentbody', template_name='llista.html'), name='Llista actors'),

	# UPDATE
	url(r'^actors/(?P<pk>\d+)/edit/$', GenericUpdate.as_view(
	model = Actor,
	template_name = 'form.html', 
	form_class = ActorForm), 
	name='update_actor'),

	# CREATE
	url(r'^actors/create/$', GenericCreate.as_view(
	model =  Actor,
	template_name = 'form.html',
	form_class = ActorForm), 
	name='actor_create'),
	
	# DETAIL
	url(r'^actors/(?P<pk>\d+)/$',GenericDetail.as_view(
	model = Person,
	template_name = 'dades.html'), 
	name='actor_detail'),

	# DELETE
	url(r'^actors/(?P<pk>\d+)/delete/$',GenericDelete.as_view(
	model = Actor,
	template_name = 'form.html', 
	success_url = '/actors'),
	name='actor_delete'),

#-------------------------------------------------DIRECTOR-----------------------------------------------
	
	# LIST
	url(r'^directors$', ListView.as_view(queryset=Director.objects.filter(),context_object_name='contentbody', template_name='llista.html'), name='Llista directors'),

	# UPDATE
	url(r'^directors/(?P<pk>\d+)/edit/$', GenericUpdate.as_view(
	model = Director,
	template_name = 'form.html', 
	form_class = DirectorForm), 
	name='update_director'),

	# CREATE
	url(r'^directors/create/$', GenericCreate.as_view(
	model =  Director,
	template_name = 'form.html',
	form_class = DirectorForm), 
	name='director_create'),
	
	# DETAIL
	url(r'^directors/(?P<pk>\d+)/$',GenericDetail.as_view(
	model = Person,
	template_name = 'dades.html'), 
	name='director_detail'),

	# DELETE
	url(r'^directors/(?P<pk>\d+)/delete/$',GenericDelete.as_view(
	model = Director,
	template_name = 'form.html', 
	success_url = '/directors'),
	name='director_delete'),

#-------------------------------------------------REPRESENTACIO-----------------------------------------------
	
	# LIST
	url(r'^representacions$', ListView.as_view(queryset=Representacio.objects.filter(),context_object_name='contentbody', template_name='llista.html'), name='Llista representacions'),

	# UPDATE
	url(r'^representacions/(?P<pk>\d+)/edit/$', GenericUpdate.as_view(
	model = Representacio,
	template_name = 'form.html', 
	form_class = RepresentacioForm,
	success_url = '/representacions'), 
	name='update_representacio'),
	
	url(r'^representacions/(?P<pk>\d+)/directors/(?P<pkr2>\d+)/edit/$',GenericUpdate.as_view(
	model = Director,
	template_name = 'form.html'), 
	name='representacio_update2'),

	# CREATE
	url(r'^representacions/create/$', GenericCreate.as_view(
	model =  Representacio,
	template_name = 'form.html',
	form_class = RepresentacioForm,
	success_url = '/representacions'), 
	name='representacio_create'),
	
	# DETAIL
	url(r'^representacions/(?P<pk>\d+)/$',RepresentacioDetail.as_view(),
	name='representacio_detail'),
	
	# DETAIL DIRECTOR
	url(r'^representacions/(?P<pk>\d+)/directors/(?P<pkr2>\d+)/$',GenericDetail.as_view(
	model = Person,
	template_name = 'dades.html'), 
	name='representacio_detail2'),
	# DETAIL ACTORS
	url(r'^representacions/(?P<pk>\d+)/actors/(?P<pkr3>\d+)/$',GenericDetail.as_view(
	model = Person,
	template_name = 'dades.html'), 
	name='representacio_detail3'),


	# DELETE
	url(r'^representacions/(?P<pk>\d+)/delete/$',GenericDelete.as_view(
	model = Representacio,
	template_name = 'form.html', 
	success_url = '/representacions'),
	name='representacio_delete'),

#-------------------------------------------------OBRA TEATRE-----------------------------------------------
	
	# LIST
	url(r'^obresTeatre$', ListView.as_view(queryset=Obra_Teatre.objects.filter(),context_object_name='contentbody', template_name='llista.html'), name='Llista obres Teatre'),

	# UPDATE
	url(r'^obresTeatre/(?P<pk>\d+)/edit/$', GenericUpdate.as_view(
	model = Obra_Teatre,
	template_name = 'form.html', 
	form_class = Obra_TeatreForm,
	success_url = '/obresTeatre'), 
	name='update_obraTeatre'),

	url(r'^obresTeatre/(?P<pk>\d+)/escriptors/(?P<pkr2>\d+)/edit/$',GenericUpdate.as_view(
	model = Escriptor,
	template_name = 'form.html'), 
	name='update_obraTeatre'),

	# CREATE nom_Obra
	url(r'^obresTeatre/create/$', GenericCreate.as_view(
	model =  nom_Obra,
	template_name = 'form.html',
	form_class = nom_ObraForm,
	success_url = '/obresTeatre/createObra/'), 
	name='obraTeatre_create'),
	

	# CREATE
	url(r'^obresTeatre/createObra/$', GenericCreate.as_view(
	model =  Obra_Teatre,
	template_name = 'form.html',
	form_class = Obra_TeatreForm,
	success_url = '/obresTeatre'), 
	name='obraTeatre_create2'),

	
	# DETAIL
	url(r'^obresTeatre/(?P<pk>\d+)/$',GenericDetail.as_view(
	model = Obra_Teatre,
	template_name = 'infoObresTeatre.html'), 
	name='obra_Teatre_detail'),

	# DETAIL ESCRIPTOR
	url(r'^obresTeatre/(?P<pk>\d+)/escriptors/(?P<pkr2>\d+)/$',GenericDetail.as_view(
	model = Person,
	template_name = 'dades.html'), 
	name='obra_Teatre_detail'),
	
	# DELETE
	url(r'^obresTeatre/(?P<pk>\d+)/delete/$',GenericDelete.as_view(
	model = Obra_Teatre,
	template_name = 'form.html', 
	success_url = '/obresTeatre'),
	name='obraTeatre_delete'),

 # ex: /myrestaurants/restaurants/1/reviews/create/
	url(r'^representacio/(?P<pk>\d+)/reviews/create/$',
	'views.review',
	name='review_create'),
		


	# ERROR, in logging
	url(r'^accounts/login/$',error,name='error'),

	url(r'^login/$','django.contrib.auth.views.login'),
	#url(r'^Teatre/', include('Teatre.foo.urls')),

	# Uncomment the admin/doc line below to enable admin documentation:
	#url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
)

#-------------------------------------------------RESTful API-----------------------------------------------

urlpatterns += patterns('',

	url(r'^api/escriptors/$', APIEscriptorList.as_view(), name='escriptor-list'),
	url(r'^api/escriptors/(?P<pk>\d+)/$', APIEscriptorDetail.as_view(), name='escriptor-detail'),

	url(r'^api/actors/$', APIActorList.as_view(), name='actor-list'),
	url(r'^api/actors/(?P<pk>\d+)/$', APIActorDetail.as_view(), name='actor-detail'),

	url(r'^api/directors/$', APIDirectorList.as_view(), name='director-list'),
	url(r'^api/directors/(?P<pk>\d+)/$', APIDirectorDetail.as_view(), name='director-detail'),

	url(r'^api/representacions/$', APIRepresentacioList.as_view(), name='representacio-list'),
	url(r'^api/representacions/(?P<pk>\d+)/$', APIRepresentacioDetail.as_view(), name='representacio-detail'),

	url(r'^api/obresTeatre/$', APIObra_TeatreList.as_view(), name='obra_Teatre-list'),
	url(r'^api/obresTeatre/(?P<pk>\d+)/$', APIObra_TeatreDetail.as_view(), name='obra_Teatre-detail'),

	url(r'^api/nomObra/$', APInom_ObraList.as_view(), name='nom_obra-list'),
	url(r'^api/nomObra/(?P<pk>\d+)/$',APInom_ObraDetail.as_view(), name='nom_obra-detail'),
    
    
)

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['api' ,'json', 'xml'])
