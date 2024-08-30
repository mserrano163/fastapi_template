From python:3.10-slim

WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt

CMD ["uvicorn", "app:your_app_name", "--host", "0.0.0.0", "--port", "8000"]