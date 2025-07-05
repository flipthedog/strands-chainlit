from strands.models.bedrock import BedrockModel
from strands.agent import Agent

from strands_tools import calculator

class DemoAgent():
    
    def __init__(self):
        self.model = BedrockModel(model_id="us.amazon.nova-lite-v1:0", region_name="us-east-2")
        self.agent = Agent(model=self.model, 
                           tools=[calculator],
                           callback_handler=None)

    async def process_streaming_response(self, message: str):
        agent_stream = self.agent.stream_async(message)
        async for event in agent_stream:
            yield event
    