from fastapi import File, UploadFile, HTTPException

from ocr.api.message import ocr_router
from ocr.api.message.openai_request import generate_report
from ocr.api.message.schemas import OcrResponse
from ocr.api.message.utils import divide_images, clean_response, extract_text_from_images
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
        text_content = extract_text_from_images(images)
        response = await generate_report(text_content)
        return OcrResponseWrapper(data=OcrResponse(text=clean_response(response)))
    finally:
        await file.close()
