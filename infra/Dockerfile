FROM python:3.11.5-slim

RUN mkdir /vtoroe_dyhanie
COPY requirements.txt /vtoroe_dyhanie
COPY /src/ /vtoroe_dyhanie/
WORKDIR /vtoroe_dyhanie
RUN pip3 install -r requirements.txt --no-cache-dir
CMD ["python3", "application.py"]
