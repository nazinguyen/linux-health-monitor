FROM python:3.9-slim
WORKDIR /app
RUN pip install prometheus-client
# Copy file exporter mới vào (chú ý tên file trong thư mục src của bạn)
COPY src/log_exporter.py /app/log_exporter.py
CMD ["python", "/app/log_exporter.py"]
