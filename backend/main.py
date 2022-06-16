import os

import strawberry
from dotenv import load_dotenv
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from strawberry.types import Info

from backend import store_speedtest_results
from backend.auth import authenticate
from backend.errors import AuthenticationError
from backend.register import register_user
from backend.storage.database import MongoInterface

load_dotenv()


@strawberry.type
class Mutation:
    @strawberry.field
    def register(self) -> str:
        db = MongoInterface(
            user=os.environ["MONGO_USER"], password=os.environ["MONGO_PW"]
        )
        return register_user(db=db)

    @strawberry.mutation
    def store_speedtest_results(
        self,
        speedtest_result: store_speedtest_results.AddSpeedtestResultInput,
        info: Info
    ) -> store_speedtest_results.SpeedtestResult:
        db = MongoInterface(
                user=os.environ["MONGO_USER"], password=os.environ["MONGO_PW"]
            )
        req = info.context["request"]
        user_ref = req.headers["user_ref"]
        if authenticate(user_ref=user_ref, db=db):
            return store_speedtest_results.store_speedtest_results(
                speedtest_result=speedtest_result,
                user_ref=user_ref,
                db=db
            )
        else:
            raise AuthenticationError("Authentication failed, please provide a valid user_ref in your headers.")


schema = strawberry.Schema(Mutation)

graphql_app = GraphQLRouter(schema)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(graphql_app, prefix="/graphql")
