from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from fastapi.responses import JSONResponse

from openai.controller.request_form.openai_request_form import OpenAITalkRequestForm
from openai.service.openai_service_impl import OpenAIBasicServiceImpl

openAIRouter = APIRouter()

async def injectOpenAIBasicService() -> OpenAIBasicServiceImpl:
    return OpenAIBasicServiceImpl()

@openAIRouter.post("/openai")
async def talkWithOpenAI(openAITalkRequestForm: OpenAITalkRequestForm,
                         openAIBasicService: OpenAIBasicServiceImpl =
                         Depends(injectOpenAIBasicService)):

    print(f"controller -> talkWithOpenAI(): openAITalkRequestForm: {openAITalkRequestForm}")

    openAIGeneratedText = await openAIBasicService.testai(openAITalkRequestForm.userInput)

    return JSONResponse(content=openAIGeneratedText, status_code=status.HTTP_200_OK)