import os
import warnings

os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

warnings.filterwarnings("ignore")

from transformers import logging

#BERT self attention model for My Laptop is not charging

from transformers import BertTokenizer, BertModel

text = "My Laptop is not charging"
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

inputs = tokenizer(text, return_tensors='pt')
outputs = model(**inputs)

print("BERT Self-Attention Outputs:")
print(outputs.last_hidden_state)
