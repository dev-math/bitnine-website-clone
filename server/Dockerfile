FROM python

WORKDIR /opt/api

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y netcat-traditional

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./entrypoint.sh .
RUN chmod +x /opt/api/entrypoint.sh

COPY . .

ENTRYPOINT ["/opt/api/entrypoint.sh"]
