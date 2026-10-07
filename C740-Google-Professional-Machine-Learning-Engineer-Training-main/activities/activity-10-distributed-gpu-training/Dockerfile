FROM pytorch/pytorch:2.4.1-cuda12.1-cudnn9-runtime
COPY train_distributed.py /trainer/
ENTRYPOINT ["python","-m","torch.distributed.run","/trainer/train_distributed.py"]
