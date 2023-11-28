FROM python:3.11.6-slim

WORKDIR /vtoroe_dyhanie
COPY requirements.txt ./
RUN pip3 install -r ./requirements.txt --no-cache-dir
COPY ./ ./
CMD ["python3", "src/application.py"]


# From feature33 - to be added later
#
# WORKDIR /vtoroe_dyhanie/
#
# COPY requirements.txt /vtoroe_dyhanie/
# COPY src/ /vtoroe_dyhanie/src/
#
# RUN pip3 install -r requirements.txt --no-cache-dir
# RUN python3 src/admindjango_bot/manage.py makemigrations admin_bot
# RUN python3 src/admindjango_bot/manage.py migrate
#
# CMD ["sh", "-c", "sleep 10 && python3 src/application.py"]
