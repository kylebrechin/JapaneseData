# JapaneseData


### core_1000.csv

Vocabulary from the core 100 site, prepared to be processed into a json

### core_vocabulary.json

A list of all the iKnow Core vocabulary

### formatter.py

Formatting data from the iKnow core site
- Removes newlines
- Removes brackets
- Fixes lines with no kanji, only kana

### grammar

A list of all the grammar types found in the iKnow core vocabulary, used for positional sorting in formatter.py

### test.py

Testing code on learning how to read and write from .csv and .json files
