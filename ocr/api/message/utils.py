import re

from ocr.core.config import settings


async def clean_assistant_response(thread_id: str, run_id: str):
    result = ''
    async for message in settings.OPENAI_CLIENT.beta.threads.messages.list(thread_id=thread_id, run_id=run_id):
        message_content = message.content[0].text
        annotations = message_content.annotations
        for annotation in annotations:
            message_content.value = message_content.value.replace(annotation.text, f"")
        result = message_content.value
    try:
        result = re.search(r'```markdown\s*(.*?)\s*```', result, re.DOTALL).group(1)
    except Exception as e:
        pass
    return result
