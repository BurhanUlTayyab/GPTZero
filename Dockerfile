FROM pytorch/pytorch:1.10.0-cuda11.3-cudnn8-runtime
RUN apt-get update && apt-get install -y redis

ENV TZ=Etc
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY requirements.txt /GPTZero/requirements.txt
WORKDIR /GPTZero
RUN pip install -r requirements.txt

# Instead of copying the code the source code should be mounted
COPY . /GPTZero

EXPOSE 80
# ENV port=8084
ENTRYPOINT ["python3", "main.py"]
