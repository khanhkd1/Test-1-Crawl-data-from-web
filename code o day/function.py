from bs4 import BeautifulSoup
import urllib.request
from testFun import post, getComment


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
	reviews = soup.find('div', id="bookReviews").findAll('div', class_="friendReviews elementListBrown")
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
		data_review['name_user'] = name.get('name')
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


def inputToDB(arrData):
	for data in arrData:
		post(data)
