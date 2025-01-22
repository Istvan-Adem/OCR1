import asyncio
import io

from starlette.datastructures import UploadFile

from ocr.api.message.prompts import OCRPrompts
from ocr.api.message.utils import clean_assistant_response
from ocr.core.config import settings


async def analyze_uploaded_document(file: UploadFile):
    contents = await file.read()
    openai_file = io.BytesIO(contents)
    openai_file.name = file.filename
    thread, openai_file = await asyncio.gather(
        settings.OPENAI_CLIENT.beta.threads.create(),
        settings.OPENAI_CLIENT.files.create(purpose='assistants', file=openai_file)
    )
    await settings.OPENAI_CLIENT.beta.threads.messages.create(
        attachments=[{"file_id": openai_file.id, "tools": [{"type": "file_search"}]}],
        thread_id=thread.id,
        role="user",
        content='Generate a report on the attached document'
    )
    run = await settings.OPENAI_CLIENT.beta.threads.runs.create_and_poll(
        assistant_id=settings.ASSISTANT_ID, thread_id=thread.id, instructions=OCRPrompts.generate_general_answer
    )
    return await clean_assistant_response(thread.id, run.id)
