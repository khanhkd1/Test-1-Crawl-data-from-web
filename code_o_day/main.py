# -*- coding: utf-8 -*-
from function import crawlDataFromWeb
from getNameAndAddress import nameAndAddressToFile, loadJsonWordFile


# crawlDataFromWeb('https://www.goodreads.com/author/list/4634532.Nguy_n_Nh_t_nh?page=1&per_page=30')
# print("Đã lấy xong dữ liệu và lưu tại trong folder code_o_day/data")

nameAndAddressToFile()
print('Đã tách ra tên người và địa điểm, lưu tại code_o_day/nameAndAddr')








# print((loadJsonWordFile()))











# xu li review all language, english, tieng viet
# from bs4 import BeautifulSoup
# import urllib.request
# import requests

# page1 = requests.get('https://www.goodreads.com/book/reviews/10925109?utf8=%E2%9C%93&language_code=')
# page1 = page1.content.decode("utf-8").replace('Element.update("reviews", "', '')[:-3]
# page1 = page1.replace('\\u003c', '<').replace('\\u003e', '>').replace('\\u0026', '&')
# page1 = page1.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>').replace('&quot;', '"').replace( '&#39;', "'").replace('\\', '').replace('\\n', '')
# soup = BeautifulSoup(page1, 'html.parser')
# reviews = soup.find('div', id="bookReviews").findAll('div', class_="friendReviews elementListBrown")
# print(reviews[0].text)

# def xuLyURL(url):
# 	url = url[url.index("'")+1:]
# 	url = url[:url.index("'")]
# 	return 'https://www.goodreads.com/book/show' +url[13:]

# def xuLyPageReview(url):
# 	urls = [url]
# 	page1 = requests.get(url)
# 	page1 = page1.content.decode("utf-8").replace('Element.update("reviews", "', '')[:-3]
# 	page1 = page1.replace('\\u003c', '<').replace('\\u003e', '>').replace('\\u0026', '&')
# 	page1 = page1.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>').replace('&quot;', '"').replace( '&#39;', "'").replace('\\', '').replace('\\n', '')
# 	soup = BeautifulSoup(page1, 'html.parser')
# 	try:
# 		reviews = soup.find('div', class_="uitext", style="float: right; margin-top: 10px").findAll('a')
# 		reviews = reviews[:-1]
# 		for rv in reviews:
# 			urls.append(xuLyURL(rv.get('onclick')))
# 	except:
# 		pass
# 	return urls

# print(xuLyPageReview('https://www.goodreads.com/book/reviews/10925109?utf8=%E2%9C%93&language_code='))