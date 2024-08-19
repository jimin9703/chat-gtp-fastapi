import os

from dotenv import load_dotenv
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from exponential_regression.controller.exponential_regression_controller import exponentialRegressionRouter

from exponenetial_regression.controller.exponential_regression_controller import exponentialRegressionRouter

app = FastAPI()
app.include_router(exponentialRegressionRouter)

app.include_router(exponentialRegressionRouter)

load_dotenv()

origins = os.getenv("ALLOWED_ORIGINS", "").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)