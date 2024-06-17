#FROM nvidia/cuda:12.3.2-base-ubuntu20.04
#FROM python:3
FROM python
#
#RUN apt-get update && apt-get install -y \
#    --no-install-recommends \
#    libcublasLt.so.11 \
#    python3 \
#    python3-pip \
#    libgl1-mesa-glx \
#    libglib2.0-0 \
#    libsm6 \
#    libxext6 \
#    libxrender-dev

#ENV CUDA_ENABLED=True
#ENV WEIGHTS_DIR=../config/best.onnx
WORKDIR /app

COPY requirements.txt .
RUN pip3 install opencv-python
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .
#ENV SERVER_MODE=grpc
#ENV PYTHONPATH=$PYTHONPATH:/app
#EXPOSE 5000
#EXPOSE 50051

#RUN chmod +x entrypoint.sh
#CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "5000"]
#CMD ["python", "gRCP_Server/server.py"]

#CMD ["sh", "-c", "if [ \"$SERVER_MODE\" = \"grpc\" ]; then python gRCP_Server/server.py; else uvicorn api:app --host 0.0.0.0 --port 5000; fi"]
#CMD ["./entrypoint.sh"]
CMD ["python3", "./batch.py"]
