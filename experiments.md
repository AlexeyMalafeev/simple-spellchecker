# Experiments

## Ideas
- [x] attempt to correct bigrams not in self.freqs2 (bad)
- [x] no replacement based only on unigram frequency (good)
- [ ] try skip-grams
- [ ] don't check non-cyrillic words
- [ ] add hyphen to supported transformations
- [ ] add vowel collapsing to transformations
- [ ] add support for splitting words? (transformations)
- [ ] heuristics to ignore names?
- [ ] prior probability of an unknown word that is not a typo
- [ ] error analysis
- [ ] edit distance 2?
- [ ] other typical errors to transformations? ца -> тся etc.
- [ ] ngram frequency cut off? there are typos in ngrams (видется)

## Current Best
ACC 0.4569

## 9
590c262c5fc90d998a843046e67d273c598f57fe
SimpleSpellcheckerV2, but don't rely on unigrams only when replacing  
ACC 0.4097 (+0.2121 over regular SimpleSpellcheckerV2!)

## 8
SimpleSpellcheckerSkipShort, but don't rely on unigrams only when replacing  
ACC 0.4569 (same as without skipping short)

## 7

SimpleSpellchecker, but don't rely on unigrams only when replacing  
ACC 0.4569 (+0.0159, new current best)

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

