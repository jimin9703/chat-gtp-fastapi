import json
import queue

from openai.repository.openai_repository import OpenAIRepository


class OpenAIRepositoryImpl(OpenAIRepository):
    def getResult(self, userDefinedReceiverFastAPIChannel):
        print(f"OpenAIRepositoryImpl getResult()")

        try:
            receivedResponseFromSocketClient = userDefinedReceiverFastAPIChannel.get(False)
            return json.loads(receivedResponseFromSocketClient)

        except queue.Empty:
            return "아직 데이터를 처리 중이거나 요청한 데이터가 없습니다"