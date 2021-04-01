import pandas as pd

df = pd.read_csv("data/raw/gne-release-v1.0.tsv", sep="\t", encoding="utf-8")
headlines = list(df["headline"])


def clean(hdln):
    hdln = hdln.replace("'", "")
    hdln = hdln.replace('"', "")
    hdln = hdln.replace("…", "")
    hdln = hdln.replace("”", "")
    hdln = hdln.replace("`", "")
    hdln = hdln.replace("’", "")
    hdln = hdln.replace("“", "")
    hdln = hdln.replace("(", "")
    hdln = hdln.replace(")", "")
    hdln = hdln.replace("#", "")
    return hdln

headlines = [e.strip() for e in headlines]
headlines = [e.split("|")[0] for e in headlines]
headlines = [clean(e) for e in headlines]
headlines = "\n".join(headlines)

with open("data/clean/headlines.txt", "w") as outfile:
    outfile.write(headlines)
