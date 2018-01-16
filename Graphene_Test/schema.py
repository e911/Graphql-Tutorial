import graphene
from first.schema import Query as starwars_query


class Query(starwars_query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)

