import graphene
from graphene_django.types import DjangoObjectType

from first.models import StarWars


class StarWarsObjectType(DjangoObjectType):
    class Meta:
        model = StarWars


class Query(graphene.ObjectType):
    name_list = graphene.List(StarWarsObjectType)
    a_name_list = graphene.Field(StarWarsObjectType,id=graphene.Int())

    def resolve_name_list(self, info):
        return StarWars.objects.all()

    def resolve_a_name_list(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return StarWars.objects.get(id=id)

        return None

