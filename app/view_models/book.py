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
