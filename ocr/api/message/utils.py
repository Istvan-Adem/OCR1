import base64
import io
import re

import pytesseract
from PIL import Image
from pdf2image import convert_from_bytes


def divide_images(contents: bytes) -> list[bytes]:
    images = convert_from_bytes(contents, dpi=250)
    image_bytes_list = []
    for image in images:
        img_byte_array = io.BytesIO()
        image.save(img_byte_array, format='PNG')
        img_byte_array.seek(0)
        image_bytes_list.append(img_byte_array.read())
    return image_bytes_list


def extract_text_from_images(images: list[bytes]) -> str:
    extracted_texts = []

    for image_bytes in images:
        image = Image.open(io.BytesIO(image_bytes))
        text = pytesseract.image_to_string(image)
        extracted_texts.append(text)

    return '\n'.join(extracted_texts)

def prepare_request_content(images: list[bytes]) -> list:
    content = [
        {"type": "text", "text": "Generate a report on the attached document"},
        *[
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64.b64encode(image).decode('utf-8')}",
                },
            }
            for image in images
        ]
    ]
    return content

def clean_response(text: str) -> str:
    try:
        text = re.search(r'```markdown\s*(.*?)\s*```', text, re.DOTALL).group(1)
    except Exception as e:
        pass
    return text
