from bs4 import BeautifulSoup
import urllib.request
import function
import json
import time
import csv

start = time.time()
url = 'https://www.goodreads.com/author/list/4634532.Nguy_n_Nh_t_nh?page=1&per_page=30'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

books = soup.find('table', class_="tableList").findAll('tr', itemtype="http://schema.org/Book")

sum = []
for feed in books:
	fee1 = feed.find('a')
	fee2 = feed.find('div', class_="u-anchorTarget")
	fee3 = feed.find('a', class_="authorName")
	title = fee1.get('title')
	link = fee1.get('href')
	id = int(fee2.get('id'))
	sum.append({'title': title, 'link': 'https://www.goodreads.com'+link, 'sach_id' : id, 'author': fee3.text})

for book in sum:
	print("Running...")
	book = function.xulyBook(book)

end = time.time()

print("time xu ly: ",(end - start))

with open('data.txt', 'w', encoding='utf8') as outfile:
	json.dump(sum, outfile, ensure_ascii=False)

with open('data.csv', 'w', encoding='utf-8') as csv_file:
	writer = csv.writer(csv_file)
	writer.writerow(['ID Sach', 'Title', 'Link', 'Author', 'Rate', 'Description', 'Review'])
	for sach in sum:
		writer.writerow([sach['sach_id'], sach['title'], sach['link'], sach['author'], sach['rate'], sach['description'], sach['review']])

choose = int(input('Du lieu da luu vao file data.txt va data.csv, chon 1 de luu vao database (khong luu chon so khac): '))
if choose == 1:
	function.inputToDB(sum)
	print("Da lu vao database.")


