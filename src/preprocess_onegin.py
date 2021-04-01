import re

with open("data/raw/onegin.txt", "r") as infile:
    txt = infile.read()

# delete notes
txt = re.sub(r"\([^)]*\)", "", txt)
txt = re.sub(r"\([^)]*\)", "", txt)


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


txt = clean_all_brackets(txt)
txt = txt.split("\n")
txt = [e.strip() for e in txt if len(e) > 10]
txt = "\n".join(txt)

with open("data/clean/onegin.txt", "w") as outfile:
    outfile.write(txt)
