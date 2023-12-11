FROM python:3.10-slim

COPY requirements.txt .

RUN apt update && \
    apt install -y git && \
    pip install -r requirements.txt && \
    pip install git+http://192.168.1.76:3000/bryant/MyMLOps.git@dev && \
    apt clean && \
    rm -rf /root/.cache/pip /var/cache/apk/* /var/lib/apt/lists/* && \
    useradd --create-home jenkins

USER jenkins

CMD ["bash"]
