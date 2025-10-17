import modal

# NOTE: apparently image is cached so only first run takes more time
image = modal.Image.debian_slim().pip_install("torch")
app = modal.App(image=image)

# https://modal.com/docs/guide/gpu#picking-a-gpu
@app.function(gpu="L40S")
def run():
    import torch
    #assert torch.cuda.is_available()

    # Courtesy of AI
    if torch.cuda.is_available():
        print("CUDA is available. GPU information:")

        # Get the number of available GPUs
        num_gpus = torch.cuda.device_count()
        print(f"Number of GPUs available: {num_gpus}")

        # Iterate through each GPU and print its details
        for i in range(num_gpus):
            print(f"\n--- GPU {i} ---")
            # Get the name of the GPU
            gpu_name = torch.cuda.get_device_name(i)
            print(f"Name: {gpu_name}")

            # Get the properties of the GPU
            gpu_properties = torch.cuda.get_device_properties(i)
            print(f"Total Memory: {gpu_properties.total_memory / (1024**3):.2f} GB")
            print(f"Compute Capability: {gpu_properties.major}.{gpu_properties.minor}")
            print(f"Multi-processor Count: {gpu_properties.multi_processor_count}")
            #print(f"CUDA Cores per Multi-processor: {gpu_properties.cuda_cores_per_multi_processor}")
            # AttributeError: 'torch._C._CudaDeviceProperties' object has no attribute 'cuda_cores_per_multi_processor'. Did you mean: 'max_threads_per_multi_processor'
            #print(f"Clock Rate: {gpu_properties.clock_rate / 1_000_000:.2f} MHz")
