FROM python:3.11.6-slim

WORKDIR /vtoroe_dyhanie
COPY requirements.txt ./
RUN pip3 install -r ./requirements.txt --no-cache-dir
COPY ./ ./
CMD ["python3", "src/application.py"]
