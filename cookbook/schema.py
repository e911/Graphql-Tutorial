from graphene import relay, AbstractType
from graphene_django.filter.fields import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

from cookbook.models import Category, Ingredient


class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ['name']
        interfaces = (relay.Node,)

class IngredientNode(DjangoObjectType):
    class Meta:
        model = Ingredient
        filter_fields = {'name' : ['exact','icontains','istartswith'],
                         'description':['exact','contains'],
                         'category':['exact'],
                         'category__name':['exact'],
                         }
        interfaces = (relay.Node,)

class Query(AbstractType):
    category = relay.Node.Field(CategoryNode)
    ingredient = relay.Node.Field(IngredientNode)

    all_category = DjangoFilterConnectionField(CategoryNode)
    all_ingredient = DjangoFilterConnectionField(IngredientNode)