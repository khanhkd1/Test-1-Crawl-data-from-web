# -*- coding: utf-8 -*-
from function import crawlDataFromWeb, xuLyPageReview
from bs4 import BeautifulSoup
import urllib.request

# crawlDataFromWeb('https://www.goodreads.com/author/list/4634532.Nguy_n_Nh_t_nh?page=1&per_page=1')
# print("OK")


# st = "new Ajax.Request('/book/reviews/10925109-cho-t-i-xin-m-t-v-i-tu-i-th?hide_last_page=true&amp;language_code=en&amp;page=2', {asynchronous:true, evalScripts:true, method:'get', parameters:'authenticity_token=' + encodeURIComponent('sKRVd30R7ngaMcoamGp4/pvJ7dGlFNauHKD87YM6xsq14qqxybkaUB8NtwltpqpY+bQWG9gE0ZZZ8XKLRJaRNw==')}); return false;"

print(xuLyPageReview('https://www.goodreads.com/book/show/10925109-cho-t-i-xin-m-t-v-i-tu-i-th'))

# def xulyBookTest(link):
# 	page = urllib.request.urlopen(link)
# 	soup = BeautifulSoup(page, 'html.parser')
# 	reviews = soup.find('div', class_="uitext", style="float: right; margin-top: 10px").findAll('a')
# 	reviews = reviews[:-1]
# 	for rv in reviews:
# 		print(rv.get('onclick'))

# xulyBookTest('https://www.goodreads.com/book/show/10925109-cho-t-i-xin-m-t-v-i-tu-i-th')