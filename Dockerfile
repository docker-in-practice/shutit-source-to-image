FROM ubuntu:14.04

RUN apt-get update
RUN apt-get install -y -qq curl git python-pip
WORKDIR /opt
RUN git clone https://github.com/ianmiell/shutit.git
WORKDIR shutit
RUN pip install -r requirements.txt

WORKDIR /opt
RUN git clone https://github.com/docker-in-practice/shutit-source-to-image
WORKDIR /opt/shutit-source-to-image
RUN /opt/shutit/shutit build --shutit_module_path /opt/shutit/library --delivery dockerfile

CMD ["/bin/bash"] 
