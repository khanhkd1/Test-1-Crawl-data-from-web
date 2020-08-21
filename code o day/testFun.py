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
				cmt = cmt.find('div', class_="mediumText reviewText")
				list_cmtEnd.append(cmt.text.replace('\n', '').strip())
			return list_cmtEnd
	except:
		return []

from flask_mysql import ConnectToDB, Sach, ReviewSach, CommentReviewSach
Session = ConnectToDB()
def post(data):
	try:
		session = Session()
		sach = Sach(
			sach_id= data['sach_id'],
			title= data['title'],
			link= data['link'],
			author= data['author'],
			rate= data['rate'],
			description= data['description']
		)
		session.add(sach)
		session.commit()
		record = session.query(Sach).filter_by(sach_id= data['sach_id']).one()
		record = record.__dict__
		if '_sa_instance_state' in record:
			del record["_sa_instance_state"]
		sach_id = record['id']
		for review in data['review']:
			review_ = ReviewSach(
				user_id= review['user_id'],
				sach_id= sach_id,
				name_user= review['name_user'],
				rate= review['rate'],
				review_content= review['review_content'],
				date_post= review['date_post']
			)
			session.add(review_)
			session.commit()
			record1 = session.query(ReviewSach).filter_by(review_content= review['review_content']).one()
			record1 = record1.__dict__
			if '_sa_instance_state' in record1:
				del record1["_sa_instance_state"]
			reviewsach_id = record1['id']
			for comment in review['comment']:
				comment_ = CommentReviewSach(
					review_sach_id= reviewsach_id,
					comment= comment
				)
				session.add(comment_)
			session.commit()
	except Exception as exp:
		print (exp)
	finally:
		session.close()


def get():
	try:
		session = Session()
		books = session.query(Sach).all()
		for i in range(len(books)):
			reivews = []
			for review in books[i].review:
				# review = standardizedData(review, ['id'])
				comments = []
				for comment in review.comment:
					comment = standardizedData(comment, ['id', 'review_sach_id'])
					comments.append(comment)
				review = standardizedData(review, ['id', 'comment'])
				review['comment'] = comments
				reivews.append(review)
			books[i] = standardizedData(books[i], ['id', 'review'])
			books[i]['review'] = reivews
		return books
	except Exception as exp:
		raise (exp)
		return "loi"
	finally:
		session.close()


def standardizedData(obj, del_param=None):
		try:
			obj = obj.__dict__
		except:
			return None
		if '_sa_instance_state' in obj:
			del obj["_sa_instance_state"]
		if del_param != None:
			for d in del_param:
				try:
					del obj[d]
				except:
					pass
		return obj
