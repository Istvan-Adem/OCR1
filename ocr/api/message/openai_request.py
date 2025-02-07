from ocr.api.message.prompts import OCRPrompts
from ocr.core.wrappers import openai_wrapper


@openai_wrapper(model='gpt-4o-mini')
async def generate_report(request_content: list[dict]):
    messages = [
        {
            "role": "system",
            "content": OCRPrompts.generate_general_answer
        },
        {
            "role": "user",
            "content": request_content
        }
    ]
    return messages
