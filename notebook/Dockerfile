FROM jupyter/base-notebook:latest

USER root 
COPY ./requirements /requirements
RUN pip install -r /requirements/local.txt
RUN apt-get update && apt-get install -y curl 
RUN jt -t monokai