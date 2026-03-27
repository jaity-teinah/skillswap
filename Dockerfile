FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p static/uploads

EXPOSE 5000

CMD ["python", "app.py"]