import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from exponential_regression.controller.exponential_regression_controller import exponentialRegressionRouter
from openai.controller.openai_controller import openAIRouter



app = FastAPI()

app.include_router(exponentialRegressionRouter)
app.include_router(openAIRouter)

load_dotenv()

origins = os.getenv("ALLOWED_ORIGINS", "").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="192.168.0.35", port=33333)