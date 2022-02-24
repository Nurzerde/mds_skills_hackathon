import random

from df_engine.core import Actor, Context
# import run_int

import regex as re
import nltk
from nltk.tokenize import sent_tokenize
# nltk.download('punkt')

def remove(lst):
    pattern1 = '[0-9]'
    pattern2 = 'Allah'
    lst = [re.sub(pattern1, '', i) for i in lst]
    return lst

with open(r'English-Quran-plain-text.txt', encoding='utf8') as f:
    txt = f.read()

tokens = sent_tokenize(txt)
tokens = remove(tokens)
tokens = list(filter(lambda i: len(i) > 7, tokens))
tokens = tokens[138:]
tokens = [re.sub('Allah', 'God', i) for i in tokens]
tokens = [re.sub(r'\n', ' ', i) for i in tokens]
target = []


with open(r'Bible.txt', encoding='utf8') as f:
    txt_2 = f.read()

tokens_2 = sent_tokenize(txt_2)
tokens_2 = remove(tokens_2)
tokens_2 = list(filter(lambda i: len(i) > 7, tokens_2))
tokens_2 = tokens_2[4:29688]
tokens_2 = [re.sub(r'\n', ' ', i) for i in tokens_2]
target = []
# word = 'evil'
# for t in tokens:
#     elem = re.findall(r"([^.]*?evil[^.]*\.)", t)
#     if elem != []:
#         target.append(elem)

def Quran(ctx: Context, actor: Actor, *args, **kwargs) -> str:
    word = ctx.last_request
    target.clear()
    for t in tokens:
        elem = re.findall(rf"([^.]*?{word}[^.]*\.)", t)
        if elem != []:
            target.append(elem)
    if target != []:
        sent = random.choice(target)
    else: sent = "No such phrase"
    return sent
    # return word

def Bible(ctx: Context, actor: Actor, *args, **kwargs) -> str:
    word = ctx.last_request
    target.clear()
    for t in tokens_2:
        elem = re.findall(rf"([^.]*?{word}[^.]*\.)", t)
        if elem != []:
            target.append(elem)
    if target != []:
        sent = random.choice(target)
    else: sent = "No such phrase"
    return sent

global res_g
res = str()

def choice():
    l = ["Quran", "Bible"]
    res = random.choice(l)
    return res

def RandP(ctx: Context, actor: Actor, *args, **kwargs) -> str:
    l = ["Quran", "Bible"]
    res = random.choice(l)
    # res_g = choice()
    if re.match(r"Quran", res):
        phrase = random.choice(tokens)
    else: phrase = random.choice(tokens_2)
    return [res, phrase]
    # return phrase