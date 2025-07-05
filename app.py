import chainlit as cl

from agent import DemoAgent

agent = DemoAgent()

@cl.on_chat_start
def start_chat():
    cl.user_session.set(
        "message_history",
        [{"role": "system", "content": "You are a helpful assistant."}],
    )


@cl.on_message
async def main(message: cl.Message):
    message_history = cl.user_session.get("message_history")
    message_history.append({"role": "user", "content": message.content})

    msg = cl.Message(content="")

    async for event in agent.process_streaming_response(message.content):
        if "data" in event:
            # Only stream text chunks to the client
            token = event["data"]
            await msg.stream_token(token)

    message_history.append({"role": "assistant", "content": msg.content})
    await msg.update()
