import os

import strawberry
from dotenv import load_dotenv
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from backend import store_speedtest_results
from backend.register import register_user
from backend.storage.database import MongoInterface

load_dotenv()


@strawberry.type
class Mutation:
    @strawberry.field
    def register(self) -> str:
        return register_user()

    @strawberry.mutation
    def store_speedtest_results(
        self,
        speedtest_result: store_speedtest_results.AddSpeedtestResultInput,
    ) -> store_speedtest_results.SpeedtestResult:
        return store_speedtest_results.store_speedtest_results(
            speedtest_result,
            MongoInterface(password=os.environ.get("MONGO_PW")),
        )


schema = strawberry.Schema(Mutation)

graphql_app = GraphQLRouter(schema)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(graphql_app, prefix="/graphql")
