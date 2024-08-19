from pydantic import BaseModel


class OpenAITalkRequestForm(BaseModel):
    userInput: str