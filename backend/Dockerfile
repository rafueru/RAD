FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r ./backend/requirements.txt

CMD ["python", "app.py"]
