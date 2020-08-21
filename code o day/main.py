# from bs4 import BeautifulSoup
# import urllib.request
from function import crawlDataFromWeb, getDataFromDatabase



choose = int(input('Chon 1 de lay data tu trong database, chon 2 de lay data tren website: '))

if choose == 1:
	getDataFromDatabase()
else:
	crawlDataFromWeb('https://www.goodreads.com/author/list/4634532.Nguy_n_Nh_t_nh?page=1&per_page=1')







