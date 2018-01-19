import graphene

import links.schema
import links.schema_relay
import users.schema


class Query(
    users.schema.Query,
    links.schema_relay.RelayQuery, 
    links.schema.Query, 
    graphene.ObjectType
):
    pass


class Mutation(
    users.schema.Mutation,
    links.schema_relay.RelayMutation,
    links.schema.Mutation,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)