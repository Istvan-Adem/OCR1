from ocr.api.message.prompts import OCRPrompts
from ocr.core.wrappers import openai_wrapper


@openai_wrapper(model='gpt-4o-mini')
async def generate_report(text: str):
    messages = [
        {
            "role": "system",
            "content": OCRPrompts.generate_general_answer
        },
        {
            "role": "user",
            "content": f"Generate a report based on this data:\n\n```\n{text}\n```"
        }
    ]
    return messages
