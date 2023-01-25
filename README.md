# GPTZero

GPTZero is an AI model with some mathematical hacks to determine if a piece of sentence fed to it is written by ChatGPT or a human being.

## The motivation for it

Recently, GPTZero got a lot of hype/traction from media to be able to determine whether a set of sentences are generated from ChatGPT. But since the implementation is closed-source, we tried to replicate what they are doing by open-sourcing the model and the weights.

## Installation
```pip install -r requirements.txt```

## Usage
### Using Python function
```python3 infer.py```
#### example
```
from model import GPT2PPL

model = GPT2PPL()

sentence = "your text here"

model(sentence)
```  
### Using Python input
```python3 local_infer.py```
#### example
```
Please enter your sentence: (Press Enter twice to start processing)
Hello World.
My name is mike.
(empty line)
```

## Acknowledgement
1. This repository is built based on the hugging face
https://huggingface.co/docs/transformers/perplexity

2. Liu, Yinhan, et al. "Roberta: A robustly optimized bert pretraining approach." arXiv preprint arXiv:1907.11692 (2019).
