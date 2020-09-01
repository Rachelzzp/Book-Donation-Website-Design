# from app.libs.helper import get_isbn

class BookViewModel:
    def __init__(self,book):
        # if not isinstance(data, dict):V
        #     data = data.__dict__
        #     data['author'] = author
        self.title = book['title']
        self.publisher = book['publisher']
        self.author = '、'.join(book['author'])
        # self.binding = book['binding']
        self.image = book['image']
        self.price = '￥' + book['price'] if book['price'] else book['price']
        # self.isbn = get_isbn(book)
        self.isbn = book['isbn']
        self.pubdate = book['pubdate']
        self.summary = book['summary']
        self.pages = book['pages']

    @property
    def intro(self):
        intros = filter(lambda x: True if x else False,
                        [self.author, self.publisher, self.price])

        return ' / '.join(intros)


class BookCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self,yushu_book,keyword):
        self.total = yushu_book.total
        self.books = [BookViewModel(book) for book in yushu_book.books]
        self.keyword = keyword

# class BookViewModel:
#     # 面向对象中：需要描述特征（类变量，实例变量），
#     #           需要描述行为（方法）
#
#     @classmethod
#     def package_single(cls, data, keyword):
#         returned = {
#             'books': [],
#             'total': 0,
#             'keyword': keyword
#         }
#         if data:
#             returned['total'] = 1
#             returned['books'] = [cls.__cut_book_date(data)]
#         return returned
#
#     @classmethod
#     def package_collection(cls, data, keyword):
#         returned = {
#             'books': [],
#             'total': 0,
#             'keyword': keyword
#         }
#         if data:
#             returned['total'] = data['total']
#             returned['books'] = [cls.__cut_book_date(book) for book in data['books']]
#         return returned
#
#     @classmethod
#     def __cut_book_date(cls, data):
#         book = {
#             'title': data['title'],
#             'publisher': data['publisher'],
#             'pages': data['pages'] or '',
#             'author': '、'.join(data['author']),
#             'price': data['price'],
#             'summary': data['summary'] or '',
#             'image': data['image']
#         }
