import torch
from huggingface_hub import hf_hub_download

def download_weights() -> str:
    """Download GPT-2 pretrained weights from Hugging Face Hub."""

    return hf_hub_download(
        repo_id="rasbt/gpt2-from-scratch-pytorch",
        filename="gpt2-small-124M.pth",
    )

def load_weights(model: torch.nn.Module) -> None:
    """Load pretrained GPT-2 weights into a model."""

    checkpoint = download_weights()
    state_dict = torch.load(checkpoint, weights_only=True)
    model.load_state_dict(state_dict)