from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework.fields import CharField
from models import *

class EscriptorSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name='escriptor-detail')
    user = CharField(read_only=True)
    class Meta:
        model = Escriptor
        fields = ('nom', 'edat', 'sexe', 'localitat', 'user')

class ActorSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name='actor-detail')
    user = CharField(read_only=True)
    class Meta:
        model = Actor
        fields = ('nom', 'edat', 'sexe', 'localitat', 'user')

class DirectorSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name='director-detail')
    user = CharField(read_only=True)
    class Meta:
        model = Director
        fields = ('nom', 'edat', 'sexe', 'localitat', 'user')

class nom_ObraSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name='nom_obra-detail')
    user = CharField(read_only=True)
    class Meta:
        model = nom_Obra
        fields = ('nomObra', 'user')

class RepresentacioSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name='representacio-detail')
    nomObra = HyperlinkedRelatedField(many=False, read_only=True, view_name='nom_obra-detail')
    actors = HyperlinkedRelatedField(many=True, read_only=True, view_name='actor-detail')
    director = HyperlinkedRelatedField(many=False, read_only=True, view_name='director-detail')
    user = CharField(read_only=True)
    class Meta:
        model = Representacio
        fields = ('nomRepresentacio', 'nomObra', 'dataInici', 'dataFi', 'actors', 'director','user')

class Obra_TeatreSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name='obra_Teatre-detail')
    nom = HyperlinkedIdentityField(view_name='nom_obra-detail')
    escriptor = HyperlinkedRelatedField(many=False, read_only=True, view_name='escriptor-detail')
    representacions = HyperlinkedRelatedField(many=True, read_only=True, view_name='representacio-detail')
    user = CharField(read_only=True)
    class Meta:
        model = Obra_Teatre
        fields = ('nom', 'Tipus', 'escriptor', 'representacions', 'user')

