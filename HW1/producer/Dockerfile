FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD req.txt /code/
RUN pip3 install -r req.txt
ADD . /code/
EXPOSE 5672
