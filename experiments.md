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

## 6
eb7f9f0ce6216a2839bbe53a97958b07af24ba98
SimpleSpellcheckerV2SkipShort - len 3  
ACC 0.2096  

## 5
51383f2bcc2845f62798c150eaf07e931c3a46d9
SimpleSpellcheckerSkipShort - skip if len <= 4  
ACC 0.442

## 4
SimpleSpellcheckerSkipShort - skip if len <= 2  
ACC 0.441

## 3
SimpleSpellcheckerSkipShort - skip if len <= 3  
ACC 0.4425 (+0.0015)

## 2

cbcfc9e3996ae9a9d9373d3121665940f88d1ede  
SimpleSpellcheckerV2 - error detection is bigram-based  
ACC 0.1976

## 1
b93d3ebab871c03bf1ddfe5fda8d4d00dfaf6da8  
SimpleSpellchecker, use all ngrams, attempt to correct only tokens that are not in self.freqs1  
ACC 0.441 

