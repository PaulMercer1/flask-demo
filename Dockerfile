FROM python:3.6-alpine

EXPOSE 5000

WORKDIR /app

# install pip updates
RUN python -m pip install --upgrade pip
COPY requirements.txt .

# install requirements
RUN pip install -r requirements.txt
COPY . .
RUN python create.py

ENTRYPOINT python app.py