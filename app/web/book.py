# 关于book的所有视图函数
import json

from flask import jsonify,request,render_template,flash
from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from . import web

# Blueprint
# 用web注册视图函数,代替用app注册
from ..view_models.book import BookViewModel,BookCollection

@web.route('/book/search')
def search():
    # q(defaulted keyword) / isbn ; page
    # 让搜索网址变成?q=金庸&page=1: 用？的传参方式
    # q = request.args['q'] # args immutable
    # page = request.args['page']

    # a = request.args.to_dict() # 可转换成可变的字典

    # 验证层: link forms/book.py
    form = SearchForm(request.args)
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)
            # dict 序列化
            # API 将数据用json格式返回客户端

        books.fill(yushu_book, q)
        # return json.dumps(books, default=lambda o: o.__dict__)
        # return jsonify(books)
    else:
        flash('Your keyword is wrong. Please enter the correct keyword!')
        # return jsonify(form.errors)
    return render_template('search_result.html', books=books, form=form)

@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.books[0])
    return render_template('book_detail.html', book=book, wishes=[], gifts=[])

@web.route('/test')
def test():
    r = {
        'name': 'ruchen',
        'age': 18
    }
    flash('hello')
    return render_template('test.html', data=r)

@web.route('/test1')
def test1():
    from flask import request
    from app.libs.none_local import n
    print(n.v)
    n.v = 2
    print(n.v)
    print('----------')
    print(getattr(request, 'v', None))
    setattr(request, 'v', 2)
    print('----------')
    return ''