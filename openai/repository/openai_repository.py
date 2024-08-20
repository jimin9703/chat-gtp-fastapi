from abc import ABC, abstractmethod


class OpenAIBasicRepository(ABC):
    def generateText(self, userInput):
        pass