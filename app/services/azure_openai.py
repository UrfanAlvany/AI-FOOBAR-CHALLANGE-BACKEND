import os
from dotenv import load_dotenv
from openai import AsyncAzureOpenAI

load_dotenv()


async def get_response_from_openai(prompt: str, model: str):
    client = AsyncAzureOpenAI(
        azure_endpoint=os.getenv("AZURE_ENDPOINT"),
        api_key=os.getenv("AZURE_API_KEY"),
        api_version="2024-02-01"  # Ensure this is the correct API version
    )

    response = await client.chat.completions.create(
        model=model,  # Use the model parameter dynamically
        messages=[{"role": "system", "content": prompt}]
    )

    return response
