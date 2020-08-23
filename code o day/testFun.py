from bs4 import BeautifulSoup
import urllib.request

def xulyUser(user):
	user = user.replace('/user/show/', '')
	user = user[:user.index('-')]
	return int(user)

def getComment(link_RV):
	try:
		soup_rv = BeautifulSoup(urllib.request.urlopen(link_RV), 'html.parser')
		list_cmt = soup_rv.findAll('div', class_="comment u-anchorTarget")
		if list_cmt == None:
			return []
		else:
			list_cmtEnd = []
			for cmt in list_cmt:
				dic = {}
				cmt = cmt.find('div', class_="mediumText reviewText")
				dic['content'] = cmt.text.replace('\n', '').strip()
				dic['user_id'] = int(cmt.find('a').get('data-resource-id'))
				dic['user_name'] = cmt.find('a').get('title')
				list_cmtEnd.append(dic)
			return list_cmtEnd
	except Exception as exp:
		print(exp)
		return []

from flask_mysql import ConnectToDB, Book, User, ReviewBook, CommentOfReview
Session = ConnectToDB()


def getUser():
	try:
		session = Session()
		users = session.query(User).all()
		for i in range(len(users)):
			users[i] = standardizedData(users[i])
		return users
	except Exception as exp:
		raise (exp)
		return []
	finally:
		session.close()

def post(data):
	try:
		addBook(data)
		book_id = getBookID(data['sach_id'])
		for review in data['review']:
			try:
				addUser(review)
			except Exception as exp:
				pass
			finally:
				user_id_review = getUserID(review['user_id'])
				addReview(review, user_id_review, book_id)
				reviewsach_id = getReviewID(review['review_content'])
				for comment in review['comment']:
					try:
						addUser(comment)
					except Exception as exp:
						raise exp
					finally:
						user_id_comment = getUserID(comment['user_id'])
						addComment(comment, reviewsach_id, user_id_comment)
	except Exception as exp:
		raise exp

def getBookID(sach_id):
	session = Session()
	book = standardizedData(session.query(Book).filter_by(book_id= sach_id).one())
	session.close()
	return book['id']

def getUserID(user_id):
	session = Session()
	user = standardizedData(session.query(User).filter_by(user_id= user_id).one())
	session.close()
	return user['id']

# def getUserName(user_id):
# 	session = Session()
# 	user = standardizedData(session.query(User).filter_by(user_id= user_id).one())
# 	session.close()
# 	return user['user_name']

def getReviewID(review_content):
	session = Session()
	review = standardizedData(session.query(ReviewBook).filter_by(review_content= review_content).one())
	session.close()
	return review['id']

def addComment(data, reviewsach_id, user_id_comment):
	session = Session()
	comment_ = CommentOfReview(
		comment_review_id= reviewsach_id,
		comment_user_id= user_id_comment,
		comment_content= data['content']
	)
	session.add(comment_)
	try:
		session.commit()
	except:
		pass
	finally:
		session.close()

def addBook(data):
	session = Session()
	book = Book(
		book_id= data['sach_id'],
		book_title= data['title'],
		book_link= data['link'],
		book_author= data['author'],
		book_rate= data['rate'],
		book_description= data['description']
	)
	session.add(book)
	try:
		session.commit()
	except:
		pass
	finally:
		session.close()

def addReview(data, user_id_review, book_id):
	session = Session()
	review_ = ReviewBook(
		review_user_id= user_id_review,
		review_book_id= book_id,
		review_rate= data['rate'],
		review_content= data['review_content'],
		review_date_post= data['date_post']
	)
	session.add(review_)
	try:
		session.commit()
	except:
		pass
	finally:
		session.close()
def getAllUser():
	session = Session()
	user = session.query(User).all()
	users = []
	for i in range(len(user)):
		user[i] = standardizedData(user[i])
		users.append(user[i]['user_id'])
	session.close()
	return users

def addUser(data):
	if data['user_id'] in getAllUser():
		pass
	else:
		session = Session()
		user = User(
			user_id= data['user_id'],
			user_name= data['user_name']
			)
		try:
			session.add(user)
			session.commit()
		except Exception as exp:
			raise exp
		finally:
			session.close()

def standardizedData(obj, del_param=None, param=None):
	data = {}
	try:
		obj = obj.__dict__
	except:
		return None
	try:
		if '_sa_instance_state' in obj:
			del obj["_sa_instance_state"]
	except:
		pass
	if del_param != None:
		for d in del_param:
			try:
				del obj[d]
			except:
				pass
	if param != None:
		for p in param:
			data[p] = obj[param[p]]
		return data

	return obj
