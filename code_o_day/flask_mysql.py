from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import *
from sqlalchemy.orm import *
from sqlalchemy import *

Base = declarative_base()


# khoi tao ket noi vao co so du lieu
def ConnectToDB():
	engine = create_engine('mysql+mysqldb://root:pass@localhost/test1_crawlData_DesignAgain?charset=utf8mb4')
	Session = sessionmaker(bind=engine)
	return Session



class Book(Base):
	__tablename__ = 'book'
	id = Column(Integer, primary_key=True)
	book_id = Column(Integer)
	book_title = Column(String)
	book_author = Column(String)
	book_link = Column(String)
	book_rate = Column(Float)
	book_description = Column(String)
	review_book = relationship('ReviewBook')

class User(Base):
	__tablename__ = 'user'
	id = Column(Integer, primary_key=True)
	user_id = Column(Integer)
	user_name = Column(String)
	review_user = relationship('ReviewBook')
	comment_user = relationship('CommentOfReview')

class ReviewBook(Base):
	__tablename__ = 'review'
	id = Column(Integer, primary_key=True)
	review_user_id = Column(Integer, ForeignKey('user.id'))
	review_book_id = Column(Integer, ForeignKey('book.id'))
	review_rate = Column(Integer)
	review_content = Column(String)
	review_date_post = Column(String)
	comment_review = relationship('CommentOfReview')

class CommentOfReview(Base):
	__tablename__ = 'comment'
	id = Column(Integer, primary_key=True)
	comment_review_id = Column(Integer, ForeignKey('review.id'))
	comment_user_id = Column(Integer, ForeignKey('user.id'))
	comment_content = Column(String)