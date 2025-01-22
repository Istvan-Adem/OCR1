    FROM python:3.12.7

RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:$PATH"

WORKDIR /app

COPY --chown=user ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN apt-get update && apt-get install -y poppler-utils

COPY --chown=user . /app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]