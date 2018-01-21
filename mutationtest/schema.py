import graphene
from graphene import relay, ObjectType
from graphene.types.inputobjecttype import InputObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

from mutationtest.models import Person
from mutationtest.utils import update_create_instance


class PersonInput(InputObjectType):
    name = graphene.String()
    age = graphene.Int()
    description = graphene.String()

class PersonNode(DjangoObjectType):
    class Meta:
        model = Person
        filter_fields = {'name':['iexact'],
                         'age':['iexact'],
                         'description':['icontains'],}
        interfaces=(relay.Node,)


class CreatePerson(relay.ClientIDMutation):

    class Input:
        person = graphene.Argument(PersonInput)

    new_person = graphene.Field(PersonNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **inp):
        person_data = dict(name=inp.get('person').get('name'),
                           age = inp.get('person').get('age'),
                           description=inp.get('person').get('description'))
        person= Person()
        new_person = update_create_instance(person , person_data)
        return cls(new_person=new_person)


class Mutation(ObjectType):
    create_person = CreatePerson.Field()


class Query(ObjectType):
    person = relay.Node.Field(PersonNode)
    all_persons = DjangoFilterConnectionField(PersonNode)
