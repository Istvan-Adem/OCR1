from fastapi import File, UploadFile

from ocr.api.message import ocr_router
from ocr.api.message.openai_request import generate_report
from ocr.api.message.schemas import OcrResponse
from ocr.api.message.utils import divide_images, prepare_request_content, clean_response
from ocr.core.wrappers import OcrResponseWrapper


@ocr_router.post('/parse')
async def get_all_chat_messages(
        file: UploadFile = File(...)
) -> OcrResponseWrapper[OcrResponse]:
    try:
        contents = await file.read()
        images = divide_images(contents)
        request_content = prepare_request_content(images)
        response = await generate_report(request_content)
        return OcrResponseWrapper(data=OcrResponse(text=clean_response(response)))
    finally:
        await file.close()
