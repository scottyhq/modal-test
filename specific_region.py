import modal
import os

# https://modal.com/docs/guide/region-selection
app = modal.App("specify-region")


@app.function(region="westus2")
def square(x):
    print(f"running in {os.environ['MODAL_REGION']}")
    return x**2


@app.local_entrypoint()
def main():
    print("the square is", square.remote(42))
