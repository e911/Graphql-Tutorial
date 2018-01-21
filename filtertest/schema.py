import django_filters
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

#custom filter
class AnimalFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='iexact')

    class Meta:
        model = Animal
        fields = ['name', 'is_domesticated']

    @property
    def qs(self):
        # The query context can be found in self.request.
        return super(AnimalFilter, self).qs

class Query(ObjectType):
    animal = relay.Node.Field(AnimalNode)
    all_animals = DjangoFilterConnectionField(AnimalNode)
    #custom filter passed as argument
    all_animals_customfilter = DjangoFilterConnectionField(AnimalNode,
                                                           filterset_class=AnimalFilter)