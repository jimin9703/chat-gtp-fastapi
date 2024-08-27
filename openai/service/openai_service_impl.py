import os
import sys

from openai.repository.openai_repository_impl import OpenAIRepositoryImpl
from openai.service.openai_service import OpenAIService
from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'template', 'include', 'socket_server'))

from template.include.socket_server.utility.color_print import ColorPrinter


class OpenAIServiceImpl(OpenAIService):
    def __init__(self, userDefinedQueueRepository: UserDefinedQueueRepositoryImpl):
        self.__openAiRepository = OpenAIRepositoryImpl()
        self.__userDefinedQueueRepository = userDefinedQueueRepository

    def requestOpenAIResult(self):
        userDefinedReceiverFastAPIChannel = self.__userDefinedQueueRepository.getUserDefinedSocketReceiverFastAPIChannel()
        ColorPrinter.print_important_data("userDefinedReceiverFastAPIChannel", userDefinedReceiverFastAPIChannel)
        return self.__openAiRepository.getResult(userDefinedReceiverFastAPIChannel)

