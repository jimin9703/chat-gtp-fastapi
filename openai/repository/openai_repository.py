from abc import ABC, abstractmethod


class OpenAIRepository(ABC):
    @abstractmethod
    def getResult(self, userDefinedReceiverFastAPIChannel):
        pass