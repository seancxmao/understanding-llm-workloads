import torch
from huggingface_hub import hf_hub_download
from model import Qwen3Model
from config import QWEN_CONFIG_06_B

def download_weights() -> str:
    """Download Qwen3 pretrained weights from Hugging Face Hub."""

    return hf_hub_download(
        repo_id="rasbt/qwen3-from-scratch",
        filename="qwen3-0.6B-base.pth",
    )


def load_weights(model: torch.nn.Module) -> None:
    """Load pretrained Qwen3 weights into a model."""
    model_file = download_weights()
    model.load_state_dict(torch.load(model_file))
