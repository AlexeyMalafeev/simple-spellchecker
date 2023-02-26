# Experiments

## Ideas
- [ ] attempt to correct trigrams not in self.freqs3
- [ ] heuristics to ignore names?
- [ ] prior probability of an unknown word that is not a typo
- [ ] error analysis
- [ ] edit distance 2?
- [ ] add vowel collapsing to transformations
- [ ] other typical errors to transformations? ца -> тся etc.
- [ ] add support for splitting words? (transformations)
- [ ] don't check non-cyrillic words
- [ ] don't replace unknown words for unigrams if bigrams/trigrams don't support the replacement
- [ ] add hyphen to supported transformations
- [ ] frequency cut off? there are typos in ngrams (видется)

## 2


## 1
b93d3ebab871c03bf1ddfe5fda8d4d00dfaf6da8  
SimpleSpellchecker, use all ngrams, attempt to correct only tokens that are not in self.freqs1  
ACC 0.4405  

