import torch
import tiktoken

class GPT2Tokenizer:
    """A lightweight wrapper around tiktoken's GPT-2 tokenizer."""

    def __init__(self):
        self._tokenizer = tiktoken.get_encoding("gpt2")

    def encode(self, text: str) -> torch.Tensor:
        """Encode text into token IDs with a batch dimension."""
        token_ids = self._tokenizer.encode(
            text,
            allowed_special={"<|endoftext|>"},
        )
        return torch.tensor(token_ids).unsqueeze(0) # add batch dimension

    def decode(self, token_ids: torch.Tensor) -> str:
        """Decode token IDs back to text."""
        if token_ids.ndim == 2:
            token_ids = token_ids.squeeze(0) # remove batch dimension
        return self._tokenizer.decode(token_ids.tolist())

    @property
    def vocab_size(self) -> int:
        return self._tokenizer.n_vocab
