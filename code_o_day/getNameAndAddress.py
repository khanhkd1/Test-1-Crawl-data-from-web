# -*- coding: utf-8 -*-
from underthesea import pos_tag
from langdetect import detect
import pandas as pd
import nltk
import csv
import json


def loadJsonWordFile():
	with open('exceptWord.json', encoding='utf-8') as f:
		data = json.load(f)
	return set(data)


def preprocess(sent):
    sent = nltk.word_tokenize(sent)
    sent = nltk.pos_tag(sent)
    return sent


def nameAndAddressToFile():
	books = pd.read_csv('data/Books.csv').values
	description = books[:, 5].reshape(-1, 1)

	reviews = pd.read_csv('data/Reviews.csv').values
	review = reviews[:, 3].reshape(-1, 1)

	comments = pd.read_csv('data/Comments.csv').values
	comment = comments[:, 4].reshape(-1, 1)

	# myset = set()
	myset = {}

	myset = addToSet(myset, description)
	myset = addToSet(myset, review)
	myset = addToSet(myset, comment)

	# with open('nameAndAddr/data.txt', 'w', encoding='utf8') as txt_file:
	# 	for se in myset:
	# 		txt_file.write(se+"\n")

	with open('nameAndAddr/data.csv', 'w', encoding='utf8') as csv_file:
		writer = csv.writer(csv_file)
		for key, value in myset.items():
			writer.writerow([key, value])

def addToSet(myset, data):
	for text in data:
		try:
			mem = []
			if detect(text[0]) == 'vi':
				for tup in pos_tag(text[0]):
					if tup[1] == 'Np':
						if not tup[0] in loadJsonWordFile():
							mem.append(tup[0])
			else:
				nltk_tokens = preprocess(text[0])
				cp = nltk.RegexpParser('NNPs: {<NNP>?<NNP>*<NNP>}')
				cs = cp.parse(nltk_tokens)
				for i in cs:
					if not type(i) is tuple:
						if not str(i).replace('(NNPs ','').replace('/NNP', '')[:-1] in loadJsonWordFile():
							mem.append(str(i).replace('(NNPs ','').replace('/NNP', '')[:-1])
			myset[text[0]] = list(set(mem))
		except Exception as E:
			pass
	return myset


