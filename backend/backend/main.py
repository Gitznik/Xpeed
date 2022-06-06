import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from strawberry.file_uploads import Upload

import store_speedtest_results
from register import register_user


@strawberry.type
class Mutation:
    @strawberry.field
    def register(self) -> str:
        return register_user()

    @strawberry.mutation
    def store_speedtest_results(self, speedtest_result: store_speedtest_results.AddSpeedtestResultInput) -> store_speedtest_results.SpeedtestResult:
        return store_speedtest_results.store_speedtest_results(speedtest_result)

schema = strawberry.Schema(Mutation)

graphql_app = GraphQLRouter(schema)

app = FastAPI()
@app.get("/")
async def root():
    return { "message": "Hello World"}
app.include_router(graphql_app, prefix="/graphql")
