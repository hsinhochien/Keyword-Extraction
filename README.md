# spaCy
Prerequisites: <br>
1. ```pip install spacy --no-cache-dir```
2. ```python -m spacy download zh_core_web_lg``` (Download the Chinese model of spaCy)
## spaCy_ner.py
This file trains a new Chinese model from scratch. <br>
(Download the basic configuration file for NER from the official website first. ```base_config.cfg```)
## spaCy_pos_ner.py
This file trains an existing model by disabling pipelines other than NER.
