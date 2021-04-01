import re


with open("data/raw/alice.txt", "r") as infile:
    txt_alice = infile.read()

# delete notes
txt_alice = re.sub(r"\([^)]*\)", "", txt_alice)


def delete_first_brackets(text):
    start_position = text.find("[")
    end_position = text.find("]") + 1
    return text[:start_position] + " " + text[end_position:]


def clean_all_brackets(text):
    """A quick and dirty solution to delete multiline notes in brackets"""
    if "[" in text and "]" in text:
        text = delete_first_brackets(text)
        return clean_all_brackets(text)
    else:
        return text


txt_alice = clean_all_brackets(txt_alice)
txt_alice = txt_alice.split("\n")
txt_alice = [e.strip() for e in txt_alice if len(e) > 10]
txt_alice = " ".join(txt_alice)

with open("data/clean/alice.txt", "w") as outfile:
    outfile.write(txt_alice)
