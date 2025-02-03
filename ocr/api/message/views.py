from fastapi import File, UploadFile

from ocr.api.message import ocr_router
from ocr.api.message.schemas import OcrResponse
from ocr.api.message.utils import divide_images, prepare_request_content, clean_response
from ocr.core.wrappers import OcrResponseWrapper


@ocr_router.post('/parse')
async def get_all_chat_messages(
        file: UploadFile = File(...)
) -> OcrResponseWrapper[OcrResponse]:
    try:
        contents = await file.read()
        return OcrResponseWrapper(data=OcrResponse(text=clean_response("## Coming soon")))
    finally:
        await file.close()
