FROM python:3.12-slim
COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt
WORKDIR /app
COPY . /app
EXPOSE 5000
CMD ["python", "HW2_flask.py"]