import spacy
from spacy.tokens import DocBin
from spacy.util import filter_spans
from tqdm import tqdm
import json
import pandas as pd

# 創建一個空的中文模型
nlp = spacy.blank("zh")
ner = nlp.get_pipe("ner")

# 初始化 DocBin 對象
doc_bin = DocBin()

with open('training_data.json', 'r', encoding='utf-8') as f:
    training_data = json.load(f)

# 將每個訓練例子轉換為 Doc 對象並添加到 DocBin
for training_example in tqdm(training_data):
    text = training_example['text']
    entities  = training_example['entities']

    doc = nlp.make_doc(text)

    spans = []
    for entity in entities:
        start = entity['start']
        end = entity['end']
        label = entity['label']

        ner.add_label(label)

        span = doc.char_span(start, end, label=label, alignment_mode="contract")
        if span is not None:
            spans.append(span)

    filtered_spans = filter_spans(spans)
    doc.ents = filtered_spans

    doc_bin.add(doc)

# 將 DocBin 對象保存為二進制格式的文件
doc_bin.to_disk("train.spacy")

print("訓練數據已成功保存為 train.spacy 文件")

!python -m spacy init fill-config base_config.cfg config.cfg

!python -m spacy train config.cfg --output ./output --paths.train ./train.spacy --paths.dev ./train.spacy