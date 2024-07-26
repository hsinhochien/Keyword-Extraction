# Keyword Extraction
Prerequisites: <br>
1. ```pip install spacy --no-cache-dir```
2. ```python -m spacy download zh_core_web_lg``` (Download the Chinese model of spaCy)

Goal: <br>
To identify the products that consumers truly want when searching on a shopping platform.
## spaCy_ner.py
This file trains a new Chinese spaCy model from scratch. <br>
(Download the basic configuration file for NER from the official website first. ```base_config.cfg```)
## spaCy_pos_ner.py
This file trains an existing spaCy model by disabling pipelines other than NER.
