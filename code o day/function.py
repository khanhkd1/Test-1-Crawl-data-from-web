from bs4 import BeautifulSoup
import urllib.request
import urllib.error
from testFun import getComment, post, getUser
import json
import time
import csv


def crawlDataFromWeb(url):
	start = time.time()
	sum = []
	for ur in xuLyPageBook(url):
		page = urllib.request.urlopen(ur)
		soup = BeautifulSoup(page, 'html.parser')
		try:
			books = soup.find('table', class_="tableList").findAll('tr', itemtype="http://schema.org/Book")
		except:
			books = []
		for feed in books:
			fee1 = feed.find('a')
			fee2 = feed.find('div', class_="u-anchorTarget")
			fee3 = feed.find('a', class_="authorName")
			title = fee1.get('title')
			link = fee1.get('href')
			id = int(fee2.get('id'))
			sum.append({'title': title, 'link': 'https://www.goodreads.com'+link, 'sach_id' : id, 'author': fee3.text})
	for i in range(len(sum)):
		print("Running...",i)
		while True:
			try:
				sum[i] = xulyBook(sum[i])
				break
			except Exception as ex:
				print("Running again...")
	end = time.time()
	dataToText(sum)
	inputToDB(sum)
	print("time xu ly: ",(end - start))
	users = getUser()
	dataToCSV(sum, users)


# def crawlDataFromWeb(url):
# 	sum = []
# 	page = urllib.request.urlopen(url)
# 	soup = BeautifulSoup(page, 'html.parser')
# 	try:
# 		books = soup.find('table', class_="tableList").findAll('tr', itemtype="http://schema.org/Book")
# 	except:
# 		books = []
# 	for feed in books:
# 		fee1 = feed.find('a')
# 		fee2 = feed.find('div', class_="u-anchorTarget")
# 		fee3 = feed.find('a', class_="authorName")
# 		title = fee1.get('title')
# 		link = fee1.get('href')
# 		id = int(fee2.get('id'))
# 		sum.append({'title': title, 'link': 'https://www.goodreads.com'+link, 'sach_id' : id, 'author': fee3.text})
# 	for i in range(len(sum)):
# 		print("Running...",i)
# 		while True:
# 			try:
# 				sum[i] = xulyBook(sum[i])
# 				break
# 			except Exception as ex:
# 				print("Running again...")
# 	dataToText(sum)



def xulyUser(user):
	if('/user/show/' in user):
		user = user.replace('/user/show/', '')
		if '-' in user:
			user = user[:user.index('-')]
	return int(user)

def xulyBook(data):
	page = urllib.request.urlopen(data['link'])
	soup = BeautifulSoup(page, 'html.parser')
	rate = soup.find('div', id='topcol').find('div',
			id='metacol').find('div', id='bookMeta').find('span', itemprop="ratingValue")
	data['rate'] = float((rate.text))
	try:
		book = soup.find('div', id="description", class_="readable stacked").find('span', style="")
		data['description'] = book.text
	except:
		data['description'] = ''
	data['review'] = []
	for linkPage in xuLyPageReview(data['link']):
		try:
			page_ = urllib.request.urlopen(linkPage)
			soup_ = BeautifulSoup(page_, 'html.parser')
		except urllib.error.URLError as e: 
			continue
		reviews = soup_.find('div', id="bookReviews").findAll('div', class_="friendReviews elementListBrown")
		for review in reviews:
			data_review = {}
			content = review.find('div', class_="reviewText stacked").find('span',
											class_="readable").find('span', style=None)
			name = review.find('div', class_="reviewHeader uitext stacked").find('span',
																				 itemprop="author").find('a')
			date_post = review.find('div', class_="reviewHeader uitext stacked").find('a',
																  class_="reviewDate createdAt right")
			rate = review.find('div', class_="reviewHeader uitext stacked").findAll('span',
																				class_="staticStar p10")

			data_review['user_id'] = xulyUser(name.get('href'))
			data_review['user_name'] = name.get('name')
			data_review['rate'] = len(rate)
			data_review['review_content'] = content.text
			data_review['date_post'] = date_post.text
			commen = review.find('div').find('div').find('div',
			class_="left bodycol").find('div', class_="reviewFooter uitext buttons").find('div',
																					class_="updateActionLinks")
			data_review['link_review'] = 'https://www.goodreads.com' + commen.findAll('a')[-1].get('href')
			data_review['comment'] = getComment(data_review['link_review'])
			data['review'].append(data_review)
	return data

def xuLyURL(url):
	url = url[url.index("'")+1:]
	url = url[:url.index("'")]
	return 'https://www.goodreads.com/book/show' +url[13:]

def xuLyPageReview(url):
	urls = [url]
	page = urllib.request.urlopen(url)
	soup = BeautifulSoup(page, 'html.parser')
	try:
		reviews = soup.find('div', class_="uitext", style="float: right; margin-top: 10px").findAll('a')
		reviews = reviews[:-1]
		for rv in reviews:
			urls.append(xuLyURL(rv.get('onclick')))
	except:
		pass
	return urls

def xuLyPageBook(url):
	urls = [url]
	page = urllib.request.urlopen(url)
	soup = BeautifulSoup(page, 'html.parser')
	try:
		reviews = soup.find('div', class_="leftContainer").find_next('div', style="float: right").findAll('a')
		reviews = reviews[:-1]
		for rv in reviews:
			urls.append('https://www.goodreads.com' + rv.get('href'))
	except Exception as ex:
		pass
	return urls


def inputToDB(arrData):
	for data in arrData:
		post(data)


def dataToText(books):
	with open('All.txt', 'w', encoding='utf8') as txt_file:
		json.dump(books, txt_file, ensure_ascii=False)


def dataToCSV(books, users):
	with open('Books.csv', 'w', encoding='utf-8') as csv_file:
		writer = csv.writer(csv_file)
		writer.writerow(['ID Sach', 'Title', 'Link', 'Author', 'Rate', 'Description'])
		for sach in books:
			writer.writerow([sach['sach_id'], sach['title'], sach['link'], sach['author'], sach['rate'], sach['description']])

	with open('Reviews.csv', 'w', encoding='utf-8') as csv_file:
		writer = csv.writer(csv_file)
		writer.writerow(['ID User', 'Name', 'Book', 'Review', 'Rate', 'Date Post'])
		for sach in books:
			for review in sach['review']:
				writer.writerow([review['user_id'], review['user_name'], sach['title'], review['review_content'], review['rate'], review['date_post']])

	with open('Comments.csv', 'w', encoding='utf-8') as csv_file:
		writer = csv.writer(csv_file)
		writer.writerow(['ID User', 'Name', 'Book', 'Review', 'Comment'])
		for sach in books:
			for review in sach['review']:
				for comment in review['comment']:
					writer.writerow([comment['user_id'], comment['user_name'], sach['title'], review['review_content'], comment['content']])

	with open('Users.csv', 'w', encoding='utf-8') as csv_file:
		writer = csv.writer(csv_file)
		writer.writerow(['ID User', 'Name'])
		for user in users:
			writer.writerow([user['user_id'], user['user_name']])
