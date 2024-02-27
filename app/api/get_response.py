import transformers
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import os
from app.api.models import Prompt, Response

dir_path = os.path.abspath(os.path.dirname(__file__))


def load_model():
    """load the mistral model

    Returns:
        model and tokenizer for a t5 model
    """
    model_name = "mistralai/Mistral-7B-Instruct-v0.1"
    pipeline = transformers.pipeline(
        "text-generation",
        model=model_name,
        torch_dtype=torch.float16,
        device_map="auto",
    )
    return pipeline


def get_resp(pipeline, text: Prompt):
    """Mistral module which returns possible queries intents or entailment label

    Args:
        pipeline: mistral  generative model

        text (Document): 

    Returns:
        labels: Dict[List[str]]
    """

    messages = [
                {
                    "role": "user",
                    "content": text.system_prompt,
                },
                                {"role": "assistant", "content":""" Yes"""},

                {"role": "user", "content":text.user_prompt
    },
            ]
    prompt = pipeline.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    outputs = pipeline(prompt, max_new_tokens=3056,
                        do_sample=True,
                        num_return_sequences=1,
                        temperature=0.3,
                          top_k=10, top_p=0.95)
    return {"text":outputs[0]["generated_text"]}
