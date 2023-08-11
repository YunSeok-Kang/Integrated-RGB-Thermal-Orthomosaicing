import torch
from tensorflow.python.client import device_lib

device = "cuda" if torch.cuda.is_available() else "cpu"
print(device)

print(torch.__version__)
print(torch.cuda.get_device_name(0) )

print(device_lib.list_local_devices())