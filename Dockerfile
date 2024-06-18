FROM ollama/ollama:0.1.37
SHELL ["/bin/bash", "-c"]

RUN apt-get update
RUN apt-get install -y python3
RUN apt-get -y install python3-pip
RUN pip install ollama
RUN pip install sentence-transformers
RUN pip install fastai
RUN pip install uvicorn
RUN pip install fastapi

WORKDIR /app

