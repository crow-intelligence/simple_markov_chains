import pickle
from collections import Counter

from nltk import ngrams
from nltk.tokenize import word_tokenize

with open("data/clean/headlines.txt", "r") as infile:
    headlines = infile.read().split("\n")

tokens = []
bigrams = []
trigrams = []
fourgrams = []
line_length = []

for line in headlines:
    line = line.lower()
    tkns = word_tokenize(line)
    line_length.append(len(tkns))
    tokens.extend(tkns)
    bgrms = list(ngrams(tkns, 2))
    bigrams.extend(bgrms)
    trgms = list(ngrams(tkns, 3))
    trigrams.extend(trgms)
    frgrms = list(ngrams(tkns, 4))
    fourgrams.extend(frgrms)

# count frequencies
token_freq = Counter(tokens)
bigram_freq = Counter(bigrams)
trigram_freq = Counter(trigrams)
four_freq = Counter(fourgrams)

token_total = sum(token_freq.values())
bigram_total = sum(bigram_freq.values())
trigram_total = sum(trigram_freq.values())
four_total = sum(four_freq.values())

# relative frequencies
token_rel_freq = {k: (v / token_total) + 1 for (k, v) in token_freq.items()}
bigram_rel_freq = {k: (v / bigram_total) + 1 for (k, v) in bigram_freq.items()}
trigram_rel_freq = {k: (v / trigram_total) + 1 for (k, v) in trigram_freq.items()}
four_rel_freq = {k: (v / four_total) + 1 for (k, v) in four_freq.items()}

with open("models/tokens_headlines.pkl", "wb") as outfile:
    pickle.dump(token_rel_freq, outfile)

with open("models/bigrams_headlines.pkl", "wb") as outfile:
    pickle.dump(bigram_rel_freq, outfile)

with open("models/trigrams_headlines.pkl", "wb") as outfile:
    pickle.dump(trigram_rel_freq, outfile)

with open("models/fourgrams_headlines.pkl", "wb") as outfile:
    pickle.dump(four_rel_freq, outfile)

print(f"The average line length is {sum(line_length)/len(line_length)}")
