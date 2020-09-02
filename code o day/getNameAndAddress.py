# -*- coding: utf-8 -*-
from underthesea import pos_tag
from langdetect import detect
import pandas as pd


def nameAndAddressToFile():
	books = pd.read_csv('data/Books.csv').values
	description = books[:, 5].reshape(-1, 1)

	reviews = pd.read_csv('data/Reviews.csv').values
	review = reviews[:, 3].reshape(-1, 1)

	comments = pd.read_csv('data/Comments.csv').values
	comment = comments[:, 4].reshape(-1, 1)

	myset = set()


	for text in description:
		try:
			if detect(text[0]) == 'vi':
				for tup in pos_tag(text[0]):
					if tup[1] == 'Np':
						myset.add(tup[0])
		except:
			pass

	for text in review:
		try:
			if detect(text[0]) == 'vi':
				for tup in pos_tag(text[0]):
					if tup[1] == 'Np':
						myset.add(tup[0])
		except:
			pass


	for text in comment:
		try:
			if detect(text[0]) == 'vi':
				for tup in pos_tag(text[0]):
					if tup[1] == 'Np':
						myset.add(tup[0])
		except:
			pass

	with open('data/test.txt', 'w', encoding='utf8') as txt_file:
		for se in myset:
			txt_file.write(se+"\n")
