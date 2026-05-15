
from openai import OpenAI
import os
client = OpenAI(
    api_key='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',
    base_url="https://api.groq.com/openai/v1",
)

async def ai_chat(savol):
    response = client.responses.create(
        input=savol,
        model="openai/gpt-oss-20b",
        )
    return response.output_text
