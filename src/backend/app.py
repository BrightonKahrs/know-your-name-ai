import asyncio
import os
from dotenv import load_dotenv

from agent_framework.azure import AzureOpenAIChatClient
from azure.identity import DefaultAzureCredential

load_dotenv()

azure_openai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
azure_openai_deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")
azure_openai_key = os.getenv("AZURE_OPENAI_KEY")

agent_instructions = """
    You are a joke teller. Always answer with a joke about cars
"""

chat_client = AzureOpenAIChatClient(
    endpoint=azure_openai_endpoint,
    deployment_name=azure_openai_deployment,
    credential=DefaultAzureCredential(),
)

agent = chat_client.create_agent(instructions=agent_instructions)

user_input = "How long is the equator?"


async def main():
    result = await agent.run(user_input)

    print(result)


if __name__ == "__main__":
    asyncio.run(main())
