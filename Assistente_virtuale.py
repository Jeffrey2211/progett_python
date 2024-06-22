import transformers
import torch

"""## Soluzione base"""

CHAT_MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.1"
EN_IT_MODEL_NAME = "Helsinki-NLP/opus-mt-en-it"
IT_EN_MODEL_NAME = "Helsinki-NLP/opus-mt-it-en"

chat_tokenizer = transformers.AutoTokenizer.from_pretrained(CHAT_MODEL_NAME)
chat_model = transformers.AutoModelForCausalLM.from_pretrained(CHAT_MODEL_NAME)

en_it_tokenizer = transformers.AutoTokenizer.from_pretrained(EN_IT_MODEL_NAME)
en_it_model = transformers.MarianMTModel.from_pretrained(EN_IT_MODEL_NAME)

it_en_tokenizer = transformers.AutoTokenizer.from_pretrained(IT_EN_MODEL_NAME)
it_en_model = transformers.MarianMTModel.from_pretrained(IT_EN_MODEL_NAME)

text = ""
history = []

while text.lower()!="addio":

  text = input("Tu: ")

  tokens = it_en_tokenizer.encode(text, return_tensors="pt")
  output = it_en_model.generate(tokens)
  prompt = it_en_tokenizer.decode(output[0], skip_special_tokens=True)

  history.append({"role":"user","content":prompt})

  tokens = chat_tokenizer.apply_chat_template(history,return_tensors="pt")
  output = chat_model.generate(tokens, max_new_tokens=100, pad_token_id=100)
  answer = chat_tokenizer.decode(output[0], skip_special_tokens=True)
  answer = answer.split("[/INST]")[-1].strip()

  history.append({"role":"assistant","content":answer})

  tokens = en_it_tokenizer.encode(answer, return_tensors="pt")
  output = en_it_model.generate(tokens)
  translation = en_it_tokenizer.decode(output[0], skip_special_tokens=True)

  print("Assistant: "+translation)



"""## Soluzione avanzata: creiamo una classe"""

MODEL_NAME = "meta-llama/Llama-2-7b-chat-hf"

import json

class Assistant:

  _SYSTEM_PROMPT = "Sei un chatbot amichevole che parla italiano, le tue risposte devono essere in italiano, no in inglese."

  def __init__(self, model_name):
    self._pipeline = transformers.pipeline("text-generation", model=model_name, model_kwargs={"torch_dtype": torch.bfloat16}, device_map="auto")
    self._history = [{"role":"system", "content":self._SYSTEM_PROMPT}]


  def ask(self, text):
    prompt = self._history
    prompt.append({"role":"user","content":text})
    output = self._pipeline(prompt)
    response = output[0]["generated_text"]
    self._history = response
    return response[-1]["content"]



assistant = Assistant(model_name=MODEL_NAME)
print(assistant.ask("Io sono Giuseppe"))
print(assistant.ask("Qual è il mio nome?"))
