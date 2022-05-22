import strawberry

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from register import register_user

@strawberry.type
class Mutation:
    @strawberry.field
    def register(self) -> str:
        return register_user()

schema = strawberry.Schema(Mutation)

graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
