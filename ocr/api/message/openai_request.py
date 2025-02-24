from ocr.api.message.prompts import OCRPrompts
from ocr.core.wrappers import openai_wrapper


@openai_wrapper(model='gpt-4o-mini')
async def generate_report(content: str):
    messages = [
        {
            "role": "system",
            "content": OCRPrompts.generate_general_answer
        },
        {
            "role": "user",
            "content": content
        }
    ]
    return messages


@openai_wrapper(model='gpt-4o-mini')
async def extract_original_text(content: str):
    messages = [
        {
            "role": "system",
            "content": OCRPrompts.extract_original_text
        },
        {
            "role": "user",
            "content": content
        }
    ]
    return messages
