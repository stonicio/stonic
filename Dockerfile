FROM python:3.6

RUN pip3.6 install ipython

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app
RUN python3.6 setup.py develop

CMD ipython3
