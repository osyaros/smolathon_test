FROM python:3.10.5
RUN apt-get update \
&& apt-get install -y python3-dev
RUN pip3 install --upgrade pip
COPY . .
RUN pip3 install -r requirements.txt
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh