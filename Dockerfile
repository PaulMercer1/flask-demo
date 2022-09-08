FROM python:3.10-alpine

EXPOSE 5000

WORKDIR /app
ENV db_connection="sqlite:///data.db"

RUN apk add build-base && \
    python -m pip install --upgrade pip
COPY requirements.txt .

# install requirements
RUN pip install -r requirements.txt --no-cache-dir
COPY . .

ENTRYPOINT python -u app.py