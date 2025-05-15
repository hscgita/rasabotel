FROM rasa/rasa:3.1

WORKDIR /app
COPY . /app

USER root
RUN pip install rasa-sdk

CMD ["run", "--enable-api", "--cors", "*"]
