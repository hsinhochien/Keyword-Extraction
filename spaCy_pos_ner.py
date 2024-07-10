import logging
FORMAT = '%(asctime)s [%(levelname)s]: %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)
import spacy
from spacy.training import Example
import json
import random
import pandas as pd
from tqdm import tqdm
import os
import yaml

with open('training_data.json', 'r', encoding='utf-8') as f:
    training_data = json.load(f)

# 讀取語言模型
nlp = spacy.load("zh_core_web_lg")
ner = nlp.get_pipe("ner")

# 添加新標註到 NER
ner.add_label("NOUN")
ner.add_label("ADJ")

# 整理訓練資料
with open('training_data.json', 'r', encoding='utf-8') as f:
    training_data = json.load(f)
train_data = []
for dic in training_data:
    text = dic.get('text')
    entity = dic.get('entities')
    entities = []
    for ele in entity:
        entities.append((ele['start'], ele['end'], ele['label']))
    
    temp = (text, {"entities": entities})
    train_data.append(temp)

##---- 訓練模型
optimizer = nlp.resume_training()
other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]

logging.info('Start training.')
with nlp.disable_pipes(*other_pipes):
    for itn in range(10):  # 訓練迭代次數
        random.shuffle(train_data)
        losses = {}
        for text, annotations in train_data:
            example = Example.from_dict(nlp.make_doc(text), annotations)
            nlp.update([example], drop=0.35, losses=losses)
        logging.info(losses)
logging.info('Fininsh training.')