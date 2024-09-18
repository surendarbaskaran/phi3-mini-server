import torch

# Check if GPU is available
gpu_available = torch.cuda.is_available()
print(f"GPU available: {gpu_available}")

if gpu_available:
    # Get the number of GPUs
    num_gpus = torch.cuda.device_count()
    print(f"Number of GPUs: {num_gpus}")

    # Get the name of the GPU
    gpu_name = torch.cuda.get_device_name(0)
    print(f"GPU Name: {gpu_name}")

    # Get the CUDA version
    cuda_version = torch.version.cuda
    print(f"CUDA Version: {cuda_version}")
else:
    print("CUDA not available")
