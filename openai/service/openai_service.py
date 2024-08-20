from abc import ABC, abstractmethod


class OpenAIBasicService(ABC):
    @abstractmethod
    def testai(self, userInput):
        pass