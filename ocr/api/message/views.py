from fastapi import File, UploadFile

from ocr.api.message import ocr_router
from ocr.api.message.openai_request import analyze_uploaded_document
from ocr.api.message.schemas import OcrResponse
from ocr.core.wrappers import OcrResponseWrapper


@ocr_router.post('/parse')
async def get_all_chat_messages(
        file: UploadFile = File(...)
) -> OcrResponseWrapper[OcrResponse]:
    response = await analyze_uploaded_document(file)
    with open('README.md', 'w') as file:
        file.write(response)
    return OcrResponseWrapper(data=OcrResponse(text=response))
