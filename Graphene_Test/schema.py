import graphene
from first.schema import Query as starwars_query
from cookbook.schema import Query as cookbook_query


class Query(starwars_query, cookbook_query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, auto_camelcase=False)

