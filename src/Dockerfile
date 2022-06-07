FROM ggvick/python3.9
USER root
RUN mkdir -p /workspace/

COPY . /workspace/

WORKDIR /workspace/

COPY requirements.txt /workspace/

RUN pip install --upgrade pip
RUN pip install  -r  /workspace/requirements.txt
RUN pip install pydub

ENTRYPOINT [ "python3", "./tts.py"]
#CMD [ "python3", "./tts.py" ]
