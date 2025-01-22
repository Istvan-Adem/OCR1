from fastapi.routing import APIRouter

ocr_router = APIRouter(
    prefix="/api/ocr", tags=["message"]
)

from . import views