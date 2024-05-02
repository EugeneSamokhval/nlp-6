from llama_cpp import Llama
from nltk import wordnet
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import torch
from transformers import pipeline
import os


signs = "!~@#$%^&*()_+<>?:.,’;[]\\|'\"\'–«‘'”`“"
pre_prompt = '"You are a helpful Real Estate assistant. You do not respond as \'User\' or pretend to be \'User\'. You only respond once as \'Real Estate Assistant\'. Be helpful and provide all information you can about real estate"'


def process_text(raw_text: str):
    pipe = pipeline("text-generation",
                    "Felladrin/Llama-160M-Chat-v1", device_map='auto')
    messages = [
        {
            "role": "system",
            "content": pre_prompt,
        },
        {"role": "user", "content": raw_text},
    ]
    prompt = pipe.tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True)
    outputs = pipe(prompt, max_new_tokens=1024, do_sample=True,
                   temperature=0.7, top_k=50, top_p=0.95)
    return outputs[0]["generated_text"]
