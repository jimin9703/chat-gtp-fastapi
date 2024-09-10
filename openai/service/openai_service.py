from abc import ABC, abstractmethod


class OpenAIService(ABC):
    @abstractmethod
    def requestOpenAIResult(self):
        pass