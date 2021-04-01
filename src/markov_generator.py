import pickle
import random

from mosestokenizer import MosesDetokenizer

# Onegin
with open("models/tokens_onegin.pkl", "rb") as infile:
    tokens_onegin = pickle.load(infile)

with open("models/bigrams_onegin.pkl", "rb") as infile:
    bigrams_onegin = pickle.load(infile)

with open("models/trigrams_onegin.pkl", "rb") as infile:
    trigrams_onegin = pickle.load(infile)

with open("models/fourgrams_onegin.pkl", "rb") as infile:
    fourgrams_onegin = pickle.load(infile)

# Alice
with open("models/tokens_alice.pkl", "rb") as infile:
    tokens_alice = pickle.load(infile)

with open("models/bigrams_alice.pkl", "rb") as infile:
    bigrams_alice = pickle.load(infile)

with open("models/trigrams_alice.pkl", "rb") as infile:
    trigrams_alice = pickle.load(infile)

with open("models/fourgrams_alice.pkl", "rb") as infile:
    fourgrams_alice = pickle.load(infile)

# headlines
with open("models/tokens_headlines.pkl", "rb") as infile:
    tokens_headlines = pickle.load(infile)

with open("models/bigrams_headlines.pkl", "rb") as infile:
    bigrams_headlines = pickle.load(infile)

with open("models/trigrams_headlines.pkl", "rb") as infile:
    trigrams_headlines = pickle.load(infile)

with open("models/fourgrams_headlines.pkl", "rb") as infile:
    fourgrams_headlines = pickle.load(infile)


# the average line length is about 7
def simple_generator(corpus, seed, n):
    assert n in [2, 3, 4]
    assert corpus in ["onegin", "alice", "headlines"]
    if corpus == "onegin":
        tokens = tokens_onegin
        bigrams = bigrams_onegin
        trigrams = trigrams_onegin
        fourgrams = fourgrams_onegin
    elif corpus == "alice":
        tokens = tokens_alice
        bigrams = bigrams_alice
        trigrams = trigrams_alice
        fourgrams = fourgrams_alice
    else:
        tokens = tokens_headlines
        bigrams = bigrams_headlines
        trigrams = trigrams_headlines
        fourgrams = fourgrams_headlines
    if seed not in tokens:
        seed = random.choice(list(tokens.keys()))
    if n == 2:
        bgms = {k: v for (k, v) in bigrams.items() if k[0] == seed}
        wds = [e[1] for e in bgms.keys()]
        if wds:
            weights = [float(e) for e in bgms.values()]
            return random.choices(population=wds, weights=weights)[0]
        else:
            return random.choices(population=list(tokens.keys()),
                                  weights=list(tokens.values()))[0]
    elif n == 3:
        tgms = {k: v for (k, v) in trigrams.items() if k[:2] == seed}
        wds = [e[2] for e in tgms.keys()]
        if wds:
            weights = [float(e) for e in tgms.values()]
            return random.choices(population=wds, weights=weights)[0]
        else:
            w = random.choice(list(tokens.keys()))
            return w
    else:
        frgms = {k: v for (k, v) in fourgrams.items() if k[:3] == seed}
        wds = [e[3] for e in frgms.keys()]
        if wds:
            weights = [float(e) for e in frgms.values()]
            return random.choices(population=wds, weights=weights)[0]
        else:
            w = random.choice(list(tokens.keys()))
            return w


line2 = [random.choice(list(tokens_headlines.keys()))]
for i in range(14):
    w = simple_generator("headlines", line2[-1], 2)
    line2.append(w)

with MosesDetokenizer("en") as detokenize:
    lines = detokenize(line2)
    lines = lines.capitalize()
print(lines)

line3 = [line2[0], line2[1]]
for i in range(12):
    w = simple_generator("headlines", (line3[-2], line3[-1]), 3)
    line3.append(w)

with MosesDetokenizer("en") as detokenize:
    lines = detokenize(line3)
    lines = lines.capitalize()
print(lines)

line4 = [line3[0], line3[1], line3[2]]
for i in range(10):
    w = simple_generator("headlines", (line4[-3], line4[-2], line4[-1]), 4)
    line4.append(w)

with MosesDetokenizer("en") as detokenize:
    lines = detokenize(line4)
    lines = lines.capitalize()
print(lines)

line = list(random.choice(list(trigrams_headlines.keys())))
for i in range(10):
    w = simple_generator("headlines", (line[-3], line[-2], line[-1]), 4)
    line.append(w)

with MosesDetokenizer("en") as detokenize:
    headline = detokenize(line)
    headline = lines.capitalize()
print(headline)
