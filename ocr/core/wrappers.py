import json
from functools import wraps
from typing import Generic, Optional, TypeVar

import pydash
from fastapi import HTTPException
from pydantic import BaseModel
from starlette.responses import JSONResponse

from ocr.core.config import settings

T = TypeVar('T')


class ErrorOcrResponse(BaseModel):
    message: str


class OcrResponseWrapper(BaseModel, Generic[T]):
    data: Optional[T] = None
    successful: bool = True
    error: Optional[ErrorOcrResponse] = None

    def response(self, status_code: int):
        return JSONResponse(
            status_code=status_code,
            content={
                "data": self.data,
                "successful": self.successful,
                "error": self.error.dict() if self.error else None
            }
        )


def exception_wrapper(http_error: int, error_message: str):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                return await func(*args, **kwargs)
            except Exception as e:
                raise HTTPException(status_code=http_error, detail=error_message) from e

        return wrapper

    return decorator


def openai_wrapper(
        temperature: int | float = 0, model: str = "gpt-4o-mini", is_json: bool = False, return_: str = None
):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs) -> str:
            messages = await func(*args, **kwargs)
            completion = await settings.OPENAI_CLIENT.chat.completions.create(
                messages=messages,
                temperature=temperature,
                n=1,
                model=model,
                response_format={"type": "json_object"} if is_json else {"type": "text"}
            )
            response = completion.choices[0].message.content
            if is_json:
                response = json.loads(response)
                if return_:
                    return pydash.get(response, return_)
            return response

        return wrapper

    return decorator


def background_task():
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs) -> str:
            try:
                result = await func(*args, **kwargs)
                return result
            except Exception as e:
                pass

        return wrapper

    return decorator
