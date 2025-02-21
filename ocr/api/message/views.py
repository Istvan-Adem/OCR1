import asyncio

from fastapi import File, UploadFile, HTTPException

from ocr.api.message import ocr_router
from ocr.api.message.openai_request import generate_report, extract_original_text
from ocr.api.message.schemas import OcrResponse
from ocr.api.message.utils import divide_images, clean_response, prepare_request_content
from ocr.core.wrappers import OcrResponseWrapper


@ocr_router.post('/parse')
async def get_all_chat_messages(
        file: UploadFile = File(...)
) -> OcrResponseWrapper[OcrResponse]:
    try:
        contents = await file.read()
        if file.filename.endswith('.pdf'):
            images = divide_images(contents)
        elif file.filename.endswith(('.jpg', ".jpeg", ".png")):
            images = [contents]
        else:
            raise HTTPException(status_code=400, detail='Unsupported file type.')
        content = prepare_request_content(images)
        original_text, response = await asyncio.gather(
            extract_original_text(content),
            generate_report(content)
        )
        return OcrResponseWrapper(data=OcrResponse(text=clean_response(response), originalText=original_text))
    finally:
        await file.close()
