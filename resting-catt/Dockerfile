FROM python:3.8.2-alpine3.11

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 9898

CMD [ "python3", "resting-catt" ]
