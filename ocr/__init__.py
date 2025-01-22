import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.staticfiles import StaticFiles

from ocr.core.config import settings
from ocr.core.wrappers import OcrResponseWrapper, ErrorOcrResponse


def create_app() -> FastAPI:
    app = FastAPI()

    from ocr.api.message import ocr_router
    app.include_router(ocr_router, tags=['message'])

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    static_directory = os.path.join(settings.BASE_DIR, 'static')
    if not os.path.exists(static_directory):
        os.makedirs(static_directory)

    app.mount(
        '/static',
        StaticFiles(directory='static'),
    )

    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(_, exc):
        return OcrResponseWrapper(
            data=None,
            successful=False,
            error=ErrorOcrResponse(message=str(exc.detail))
        ).response(exc.status_code)

    @app.get("/")
    async def read_root():
        return {"message": "Hello world!"}

    return app
