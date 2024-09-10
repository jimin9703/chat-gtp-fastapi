import os
import sys

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from openai.service.openai_service_impl import OpenAIServiceImpl
from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl
from template.include.socket_server.utility.color_print import ColorPrinter

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template', 'include', 'socket_server'))


openAIRouter = APIRouter()

async def injectOpenAIService() -> OpenAIServiceImpl:
    return OpenAIServiceImpl(UserDefinedQueueRepositoryImpl.getInstance())

@openAIRouter.get('/openai-answer')
async def requestOpenAIResult(openAIService: OpenAIServiceImpl =
                                 Depends(injectOpenAIService)):

    ColorPrinter.print_important_message("requestOpenAITestResult()")

    generatedOpenAIResult = openAIService.requestOpenAIResult()

    return JSONResponse(content=generatedOpenAIResult, status_code=status.HTTP_200_OK)