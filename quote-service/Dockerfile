FROM python:3.7
WORKDIR /usr/src/quote-service
COPY ./quote-service ./
RUN pip install --no-cache-dir -r requirements.txt
ENV PYTHONPATH=/usr/src/quote-service
RUN chmod +x start_api.sh
CMD ["./start_api.sh"]
