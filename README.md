# simple-spellchecker

Fast spelling error correction in Russian using some context information (bigrams and trigrams).

## Introduction

This is a small educational project I created for my students to demonstrate a simple solution to a real Natural Language Processing problem: 
spellchecking in Russian. 
Note that it is NOT a production-ready spellchecking system with state-of-the-art accuracy. 
It can correct some spelling errors and it works pretty fast, but it is not nearly as accurate as commercial systems like JamSpell Pro.

## Method

The approach used in this project is as follows: 

1. Given a sentence in Russian, split it into tokens while ignoring punctuation.
2. Consider each token in turn; if the token is unknown (not seen before), then attempt to replace it with a known token.
3. The choice of token is informed by word frequency, as well as limited context information (bigrams and trigrams). 
4. We rely on unigram, bigram and trigram counts obtained from the National Corpus of Russian (not part of this repo, but can be freely downloaded from https://ruscorpora.ru/page/corpora-freq/).

## Example

Let us consider two sentences in Russian:

*Мы шли по подъезду и стучались в каждую **жверь**, ожидая, что нам откроют.  
Есть такая поговорка: на ловца и **жверь** бежит.*

In both cases, there is the same incorrect token, "жверь". 
However, in the first sentence, we expect it to be replaced with "дверь", while in the second sentence, with "зверь". 
The context helps us disambiguate here:

```python
text = 'Мы шли по подъезду и стучались в каждую жверь, ожидая, что нам откроют.'
tokens = ['*', '*', 'мы', 'шли', 'по', 'подъезду', 'и', 'стучались', 'в', 'каждую', 'жверь', 'ожидая', 'что', 'нам', 'откроют', '$', '$']
unknown token = 'жверь'
candidates = {'зверь', 'уверь', 'вверь', 'дверь', 'верь', 'тверь'}
ranking = [('дверь', 10, 24, 39182), ('зверь', 0, 0, 3642), ('верь', 0, 0, 1164), ('тверь', 0, 0, 504), ('уверь', 0, 0, 22), ('вверь', 0, 0, 3)]
result = 'мы шли по подъезду и стучались в каждую дверь ожидая что нам откроют'

text = 'Есть такая поговорка: на ловца и жверь бежит.'
tokens = ['*', '*', 'есть', 'такая', 'поговорка', 'на', 'ловца', 'и', 'жверь', 'бежит', '$', '$']
unknown token = 'жверь'
candidates = {'зверь', 'уверь', 'вверь', 'дверь', 'верь', 'тверь'}
ranking = [('зверь', 96, 229, 3642), ('дверь', 0, 591, 39182), ('верь', 0, 79, 1164), ('тверь', 0, 14, 504), ('уверь', 0, 3, 22), ('вверь', 0, 0, 3)]
result = 'есть такая поговорка на ловца и зверь бежит'
```

## Usage

Make sure that you download the ngram files (1grams, 2grams and 3grams) from the above link, unzip and place them in the `data` folder. Other than that, there are no dependencies. 

You can simply do the following:

```python
from src.spellchecker import SimpleSpellchecker

speller = SimpleSpellchecker()
speller.check(<your_sentence_in_Russian>)
```

You can also run the `spell_demo.py` file.

Note that the initialization of SimpleSpellchecker is expensive and not optimized. 
After the initialization, however, the spellchecker can process thousands of sentences per second.
