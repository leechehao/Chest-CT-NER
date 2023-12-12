FROM python:3.10-slim

COPY requirements.txt .

RUN apt update && \
    apt install -y git && \
    pip install -r requirements.txt && \
    apt clean && \
    useradd --create-home jenkins

RUN pip install --no-cache-dir git+http://192.168.1.76:3000/bryant/MyMLOps.git@dev && \
    rm -rf /root/.cache/pip /var/cache/apk/* /var/lib/apt/lists/*

USER jenkins

CMD ["bash"]
