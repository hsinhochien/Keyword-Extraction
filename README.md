# spaCy
Prerequisites: <br>
1. ```pip install spacy --no-cache-dir```
2. ```python -m spacy download zh_core_web_lg```（下載中文模型）
## spaCy_ner.py
開一個新的中文模型從頭訓練 <br>
須至官網下載 ner 的基本配置檔 ```base_config.cfg```
## spaCy_pos_ner.py
對於既有的模型，關掉 ner 以外的 pipeline 進行訓練
