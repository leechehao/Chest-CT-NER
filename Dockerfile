FROM python:3.10-slim

COPY requirements.txt .

RUN apt update && \
    apt install -y --no-install-recommends git && \
    pip install -r requirements.txt && \
    pip install git+https://github.com/leechehao/HaoNLP.git && \
    apt clean && \
    rm -rf /root/.cache/pip /var/lib/apt/lists/* && \
    useradd --create-home jenkins

USER jenkins

CMD ["bash"]
