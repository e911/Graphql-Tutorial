import graphene
from first.schema import Query as starwars_query
from cookbook.schema import Query as cookbook_query
from filtertest.schema import Query as filtertest_query

class Query(starwars_query, cookbook_query, filtertest_query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, auto_camelcase=False)

