from graphene import relay
from graphene.types.objecttype import ObjectType
from graphene_django.filter.fields import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

from filtertest.models import Animal


class AnimalNode(DjangoObjectType):
    class Meta:
        model = Animal
        filter_fields = {
            'name':['exact','icontains','istartswith'],
            'is_domesticated':['exact'],
        }
        interfaces = (relay.Node,)

class Query(ObjectType):
    animal = relay.Node.Field(AnimalNode)
    all_animals = DjangoFilterConnectionField(AnimalNode)