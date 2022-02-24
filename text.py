import re

import numpy as np
# import torch
# from torch import nn
# import torch.nn.functional as F

import os
import regex as re
import nltk
from nltk.tokenize import sent_tokenize
# nltk.download('punkt')

# for f in os.listdir(r"./scenario"):
#     print(f)

# os.getcwd()

with open(r'./scenario/English-Quran-plain-text.txt', encoding='utf8') as f:
    txt = f.read()

tokens = sent_tokenize(txt)

# for t in tokens:
# print (t, "\n")

# len(text)

# print(text)
target = []
word = 'evil'
for t in tokens:
    elem = re.findall(r"([^.]*?{word}[^.]*\.)", t)
    if elem != []:
        target.append(elem)
print(target)

    # if len(target) > 0:

