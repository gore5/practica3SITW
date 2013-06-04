from django.forms import ModelForm	
from models import *	
  
class EscriptorForm(ModelForm):	
	class Meta:	
		model =	Escriptor
		exclude = ('user')	

class ActorForm(ModelForm):	
	class Meta:	
		model =	Actor
		exclude = ('user')	

class DirectorForm(ModelForm):	
	class Meta:	
		model =	Director
		exclude = ('user')	


class RepresentacioForm(ModelForm):	
	class Meta:	
		model =	Representacio
		exclude = ('user')
class Obra_TeatreForm(ModelForm):	
	class Meta:	
		model =	Obra_Teatre
		exclude = ('user')

class nom_ObraForm(ModelForm):	
	class Meta:	
		model =	nom_Obra
		exclude = ('user')
	
  
