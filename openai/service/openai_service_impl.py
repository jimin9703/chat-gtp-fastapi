from openai.repository.openai_repository_impl import OpenAIBasicRepositoryImpl
from openai.service.openai_service import OpenAIBasicService


class OpenAIBasicServiceImpl(OpenAIBasicService):
    def __init__(self):
        self.__openAiBasicRepository = OpenAIBasicRepositoryImpl()

    async def testai(self, userInput):
        return await self.__openAiBasicRepository.generateText(userInput)