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

def clean_response(text: str) -> str:
    try:
        text = re.search(r'```markdown\s*(.*?)\s*```', text, re.DOTALL).group(1)
    except Exception as e:
        pass
    return text
