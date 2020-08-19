from bs4 import BeautifulSoup
import urllib.request

def xulyUser(user):
    user = user.replace('/user/show/', '')
    user = user[:user.index('-')]
    return int(user)

def getComment(link_RV):
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

# url = 'https://www.goodreads.com/book/show/10925109-cho-t-i-xin-m-t-v-i-tu-i-th'
# page = urllib.request.urlopen(url)
# soup = BeautifulSoup(page, 'html.parser')
#
# list_comment = soup.find('div', id="bookReviews").findAll('div', class_="friendReviews elementListBrown")
# list_link = []
# for comment in list_comment:
#     name = comment.find('div', class_="reviewHeader uitext stacked").find('span', itemprop="author").find('a')
#     commen = comment.find('div').find('div').find('div',
#         class_="left bodycol").find('div', class_="reviewFooter uitext buttons").find('div', class_="updateActionLinks")
#     list_link.append('https://www.goodreads.com' + commen.findAll('a')[-1].get('href'))
# for link in list_link:
#     print(getComment(link))









from flask_mysql import ConnectToDB, Test, Sach, ReviewSach, CommentReviewSach
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
            record1 = session.query(ReviewSach).filter_by(user_id= review['user_id']).one()
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
